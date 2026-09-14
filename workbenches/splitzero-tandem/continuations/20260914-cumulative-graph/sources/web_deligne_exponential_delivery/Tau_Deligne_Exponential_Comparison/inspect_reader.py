from pathlib import Path
import json,re
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
checks=ROOT/'checks'
expected=re.findall(r'\\tag\{([^}]+)\}',(ROOT/'RESEARCH_NOTE.md').read_text())
record=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,executable_path="/usr/bin/chromium",args=["--no-sandbox"])
    for name,width,height in [('desktop',1440,1100),('mobile',430,940)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content((ROOT/'index.html').read_text(),wait_until='load')
        page.screenshot(path=str(checks/f'reader-{name}.png'),full_page=False)
        labels=page.locator('.equation-number').all_text_contents()
        actual=[s.strip()[1:-1] for s in labels]
        data=page.evaluate('''() => ({bodyWidth:document.documentElement.scrollWidth,viewport:innerWidth,math:document.querySelectorAll('math').length,displayMath:document.querySelectorAll('math[display="block"]').length,external: Array.from(document.querySelectorAll('script[src],link[rel="stylesheet"]')).map(e=>e.src||e.href),badText:document.querySelectorAll('.math.display:not(:has(math))').length})''')
        if actual!=expected:raise RuntimeError('tag mismatch')
        if data['bodyWidth']>width+2:raise RuntimeError(f'page overflow {data}')
        if errors:raise RuntimeError(errors)
        if data['badText']:raise RuntimeError('unrendered display math')
        if name=='desktop':
            target=page.get_by_role('heading',name='6. The parameter connection contains the original sum operator',exact=True)
            target.scroll_into_view_if_needed();page.screenshot(path=str(checks/'reader-connection.png'))
            target=page.get_by_role('heading',name='6.1 The exponential periods are constructed and proved to span',exact=True)
            target.scroll_into_view_if_needed();page.screenshot(path=str(checks/'reader-periods.png'))
        record.append({'layout':name,'width':width,'height':height,'tags':len(actual),'checks':data,'page_errors':errors})
        page.close()
    browser.close()
(checks/'reader-validation.json').write_text(json.dumps(record,indent=2)+'\n')

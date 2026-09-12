from pathlib import Path
import json
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parent
out=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    for name,width,height in [('desktop',1440,1100),('mobile',430,932)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        errors=[]
        page.on('pageerror',lambda err:errors.append(str(err)))
        page.set_content((root/'index.html').read_text(),wait_until='load')
        page.screenshot(path=str(root/'checks'/f'reader-{name}.png'),full_page=False)
        data=page.evaluate('''() => ({width:innerWidth, bodyWidth:document.body.scrollWidth, math:document.querySelectorAll('math').length, sections:document.querySelectorAll('section.level1').length})''')
        data.update(name=name,page_errors=errors)
        out.append(data)
        if name=='desktop':
            page.locator('section.level1').filter(has=page.locator('h1',has_text='The exact scalar formula')).first.scroll_into_view_if_needed()
            page.screenshot(path=str(root/'checks'/'reader-control.png'),full_page=False)
        page.close()
    browser.close()
(root/'checks'/'reader.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

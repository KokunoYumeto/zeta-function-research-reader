from pathlib import Path
import json
from playwright.sync_api import sync_playwright
base=Path(__file__).resolve().parent
records=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    for name,width,height in [('desktop',1400,1000),('mobile',390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        page.set_content((base/'index.html').read_text());page.wait_for_timeout(300)
        info=page.evaluate('''() => ({math:document.querySelectorAll('math').length,
            bodyWidth:document.body.scrollWidth,viewport:innerWidth,
            fallback:[...document.querySelectorAll('span.math')].filter(x=>!x.querySelector('math')).length,
            externalScripts:[...document.scripts].map(x=>x.src).filter(Boolean)})''')
        if info['bodyWidth']>width+2 or info['fallback'] or info['externalScripts']:
            raise RuntimeError(info)
        page.screenshot(path=str(base/'checks'/('reader-'+name+'.png')),full_page=False)
        if name=='desktop':
            heading=page.locator('h2').filter(has_text='Exact sum-coordinate conormal').first
            heading.scroll_into_view_if_needed()
            page.screenshot(path=str(base/'checks'/'reader-conormal.png'),full_page=False)
        records.append({'viewport':name,**info});page.close()
    browser.close()
(base/'checks'/'reader.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))

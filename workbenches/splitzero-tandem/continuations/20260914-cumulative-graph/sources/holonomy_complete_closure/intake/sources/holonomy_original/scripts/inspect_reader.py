from pathlib import Path
import json
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
reports=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    for label,width,height in [('desktop',1366,1000),('mobile',390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        html=(root/'index.html').read_text().replace('<link rel="stylesheet" href="reader.css">', '<style>'+(root/'reader.css').read_text()+'</style>')
        page.set_content(html,wait_until='load');page.wait_for_timeout(300)
        reports.append({'viewport':label,'body_scroll_width':page.evaluate('document.body.scrollWidth'),'viewport_width':width,'math_count':page.locator('math[display="block"]').count(),'external_scripts':page.locator('script[src]').count()})
        page.screenshot(path=str(root/f'checks/reader-{label}.png'))
        tag=page.locator('.eqno',has_text='(H33)').first
        tag.scroll_into_view_if_needed();page.screenshot(path=str(root/f'checks/quadratic-{label}.png'))
        page.close()
    browser.close()
(root/'checks/reader-inspection.json').write_text(json.dumps(reports,indent=2))
print(reports)

from pathlib import Path
import json
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parent
records=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for name,w,h in [('desktop',1360,1000),('mobile',430,900)]:
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
  page.set_content((root/'index.html').read_text(),wait_until='load')
  page.screenshot(path=str(root/'checks'/('reader-'+name+'.png')),full_page=False)
  data=page.evaluate('''() => ({width:innerWidth,scroll:document.documentElement.scrollWidth,math:document.querySelectorAll('math').length,eq:document.querySelectorAll('.equation').length,plainMath:document.querySelectorAll('span.math').length})''')
  records.append({'viewport':name,**data})
  if name=='desktop':
   page.locator('h2').filter(has_text='3. A quantitative').scroll_into_view_if_needed()
   page.screenshot(path=str(root/'checks'/'reader-contraction.png'),full_page=False)
  page.close()
 browser.close()
(root/'checks'/'reader.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))

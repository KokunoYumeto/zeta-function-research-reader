#!/usr/bin/env python3
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parent;html=(root/'index.html').read_text()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
 page.set_content(html,wait_until='load');page.screenshot(path=str(root/'checks/reader-desktop.png'))
 heading=page.get_by_role('heading',name='5. A sharp two-trace upper bound, with a complete proof',exact=True)
 heading.scroll_into_view_if_needed();page.screenshot(path=str(root/'checks/reader-theorem.png'))
 desktop_overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth+2')
 rect=page.locator('body>section').first.bounding_box()
 math_count=page.locator('math').count()
 mobile=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
 mobile.set_content(html,wait_until='load');mobile.screenshot(path=str(root/'checks/reader-mobile.png'))
 mobile_overflow=mobile.evaluate('document.documentElement.scrollWidth > window.innerWidth+2')
 data={'mathml_elements':math_count,'desktop_document_overflow':desktop_overflow,'desktop_main_left':rect['x'],'mobile_document_overflow':mobile_overflow,'page_errors':errs,'browser':'/usr/bin/chromium','render_input':'exact self-contained HTML via set_content; file URLs blocked by browser policy'}
 (root/'checks/reader-check.json').write_text(json.dumps(data,indent=2)+'\n')
 if desktop_overflow or mobile_overflow or errs or rect['x']<285:raise RuntimeError('reader layout check failed')
 print(data);browser.close()

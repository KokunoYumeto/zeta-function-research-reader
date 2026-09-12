from pathlib import Path
from playwright.sync_api import sync_playwright
import json
base=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1300,'height':940},device_scale_factor=1)
    page.set_content((base/'index.html').read_text(),wait_until='load');page.wait_for_timeout(800)
    page.screenshot(path=str(base/'checks/reader-desktop.png'))
    headings=page.locator('h2').all_text_contents()
    eq_count=page.locator('math[display="block"]').count()
    page.set_viewport_size({'width':420,'height':900});page.set_content((base/'index.html').read_text(),wait_until='load');page.wait_for_timeout(500)
    page.screenshot(path=str(base/'checks/reader-mobile.png'))
    widths=page.evaluate('({width:document.documentElement.clientWidth, scroll:document.documentElement.scrollWidth})')
    # Go to the actual relation layer; equations have local horizontal scrolling.
    section=page.locator('h2',has_text='3. The highest polynomial')
    if section.count():section.scroll_into_view_if_needed()
    page.screenshot(path=str(base/'checks/reader-layer.png'))
    result={'display_math_count':eq_count,'headings':headings,'mobile_width':widths,'page_horizontal_overflow':widths['scroll']>widths['width']+1}
    (base/'checks/reader-check.json').write_text(json.dumps(result,indent=2)+'\n')
    browser.close()
print(result)

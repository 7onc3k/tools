import asyncio
from pyppeteer import launch
import os

def save_content_to_file(content, url):
    filename = os.path.basename(url).replace("/", "_") + ".html"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

async def extract_links_from_navigation(page):
    return await page.evaluate('''
    () => {
        let elements = [...document.body.querySelectorAll('nav a, .nav a, .navbar a, .navigation a')];
        return elements.map(e => e.href);
    }
    ''')

async def extract_elements_with_large_text(page):
    return await page.evaluate('''
    () => {
        let elements = [...document.body.querySelectorAll('*')];
        return elements.filter(e => {
            let text = e.innerText || "";
            return text.length > 200;
        }).map(e => e.outerHTML).join("\n");
    }
    ''')

async def handle_infinite_scroll(page):
    prev_num_elements = 0
    while True:
        curr_num_elements = len(await page.querySelectorAll('body *'))
        if curr_num_elements == prev_num_elements:
            break
        prev_num_elements = curr_num_elements
        await page.evaluate('window.scrollBy(0, 1000)')
        await asyncio.sleep(2)

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://jsdoc.fancyproductdesigner.com')  # nahraďte 'URL_WEBOVE_STRANKY' skutečnou URL

    # Získání všech odkazů z navigačního prvku:
    links = await extract_links_from_navigation(page)

    for link in links:
        await page.goto(link)
        
        # Zvládnutí infinite scroll:
        await handle_infinite_scroll(page)

        # Extrahování obsahu:
        content_elements = await extract_elements_with_large_text(page)
        
        # Uložení obsahu do souboru:
        save_content_to_file(content_elements, link)
        
        print(f"Obsah z {link} uložen do souboru.")

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

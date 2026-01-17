import sys
import json

import asyncio
# 0- This library will scrap JS-loaded data from CoinMarketCap
from requests_html import AsyncHTMLSession
from pyppeteer import launch
import nest_asyncio
#import lxml_html_clean

nest_asyncio.apply()

# 1- Main route and session
root_address = "https://coinmarketcap.com"
session = AsyncHTMLSession()

# 2- The scraper function
async def scrape_coins():
    print('Coin Scrapping started...')

    
    # "pages": list to extract all the cryptocurrency data from all the pages of the CoinMarketCap website
    data = []
    pages = [f"{root_address}/?page={page_number}" for page_number in range (1,2)]
    #setup Pyppeteer manually 
    browser = await launch(headless=True)
    page = await browser.newPage()
    

    for url in pages:
        print("Scrapping page number... " + str(page))

        try: 
            await page.goto(url,{"waitUntil":"domcontentloaded", "timeout":30000})
            await page.waitForSelector('tbody tr', timeout=10000)

            rows = await page.querySelectorAll('tbody tr')

            if not rows:
                print("No data found! CoinMarketCap may have changes its structure.")
                continue

            for row in rows:
                d = {}
                columns = await row.querySelectorAll('td')

                if len(columns) > 9: 
                    #Extract rank
                    rank_element = await columns[1].querySelector('p')
                    d['rank'] = await page.evaluate('(el) => el.innerText',rank_element) if rank_element else '-'

                    #extract  name and symbol
                    name_and_sym = await columns[2].querySelectorAll('p')
                    d['name'] = await page.evaluate('(el) => el.innerText', name_and_sym[0]) if len(name_and_sym) > 0 else '-'
                    d['symbol'] = await page.evaluate('(el) => el.innerText', name_and_sym[1]) if len(name_and_sym) > 1 else '-'
                
                    #Extract price
                    price_col= await columns[3].querySelectorAll('span')
                    d['price'] = await page.evaluate('(el) => el.innerText', price_col[0]) if price_col else '-'
                    data.append(d)

            print(f"Extracted {len(data)} coins from {url}")

        except Exception as e:
            print(f"Error while scrapping {url}: {e}")

    await browser.close()
    return data

def save_json(data):
    with open('coins.json', 'w') as f:
        json.dump(data, f, indent=4) #indent=4 is for readability
    print("JSON saved!")

    
async def main():
    data = await scrape_coins() #await the scraper function
    save_json(data)
    print('Data fetching completed!')

if __name__ == '__main__':
    asyncio.run(main()) #use this one for regular python scripts


    
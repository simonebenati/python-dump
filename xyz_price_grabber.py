#bitcoin and eth daily prices monitoring

import bs4
import requests

def btc_grabber():
    btc_page = requests.get('https://www.coingecko.com/en/coins/bitcoin')
    btc_page.raise_for_status
    parsed_btc_page = bs4.BeautifulSoup(btc_page.text,'html.parser')
    #btc_price_n is the numeric value for btc , btc_price_24h is the price difference from 24h ago in %, btc_price_d checks if price is higher since the last 24h or lower
    btc_price_n = parsed_btc_page.select('body > div.container > div.tw-grid.tw-grid-cols-1.lg\:tw-grid-cols-3 > div.tw-col-span-3.md\:tw-col-span-2 > div > div.tw-col-span-2.md\:tw-col-span-2 > div.tw-grid-cols-3.tw-mb-1.md\:tw-flex > div > div.tw-text-4xl.tw-font-bold.tw-my-2.tw-flex.tw-items-center > span.tw-text-gray-900.dark\:tw-text-white.tw-text-3xl > span')
    btc_price_24h = parsed_btc_page.select('body > div.container > div.tw-grid.tw-grid-cols-1.lg\:tw-grid-cols-3 > div.tw-col-span-3.md\:tw-col-span-2 > div > div.tw-col-span-2.md\:tw-col-span-2 > div.tw-grid-cols-3.tw-mb-1.md\:tw-flex > div > div.tw-text-4xl.tw-font-bold.tw-my-2.tw-flex.tw-items-center > span.live-percent-change.tw-ml-2.tw-text-xl > span')
    btc_price_d = parsed_btc_page.select('#general > div.row.no-gutters.md\:tw-mt-6 > div.col-lg-8.pr-md-3 > div.my-4 > div:nth-child(2) > div:nth-child(2) > span')


    if 'text-green' in str(btc_price_d):
        print("BTC Current Value is: %s. In the last 24h it went up by: %s" % (((str(btc_price_n[0].text).strip()),str(btc_price_24h[0].text).strip())))
    else:
        print("BTC Current Value is: %s. In the last 24h it went down by: %s" % (((str(btc_price_n[0].text).strip()),str(btc_price_24h[0].text).strip())))

def eth_grabber():
    eth_page = requests.get('https://www.coingecko.com/en/coins/ethereum')
    eth_page.raise_for_status
    parsed_eth_page = bs4.BeautifulSoup(eth_page.text,'html.parser')
    #eth_price_n is the numeric value for eth , eth_price_24h is the price difference from 24h ago in %, eth_price_d checks if price is higher since the last 24h or lower
    eth_price_n = parsed_eth_page.select('body > div.container > div.tw-grid.tw-grid-cols-1.lg\:tw-grid-cols-3 > div.tw-col-span-3.md\:tw-col-span-2 > div > div.tw-col-span-2.md\:tw-col-span-2 > div.tw-grid-cols-3.tw-mb-1.md\:tw-flex > div > div.tw-text-4xl.tw-font-bold.tw-my-2.tw-flex.tw-items-center > span.tw-text-gray-900.dark\:tw-text-white.tw-text-3xl > span')
    eth_price_24h = parsed_eth_page.select('body > div.container > div.tw-grid.tw-grid-cols-1.lg\:tw-grid-cols-3 > div.tw-col-span-3.md\:tw-col-span-2 > div > div.tw-col-span-2.md\:tw-col-span-2 > div.tw-grid-cols-3.tw-mb-1.md\:tw-flex > div > div.tw-text-4xl.tw-font-bold.tw-my-2.tw-flex.tw-items-center > span.live-percent-change.tw-ml-2.tw-text-xl > span')
    eth_price_d = parsed_eth_page.select('#general > div.row.no-gutters.md\:tw-mt-6 > div.col-lg-8.pr-md-3 > div.my-4 > div:nth-child(2) > div:nth-child(2) > span')
    
    if 'text-green' in str(eth_price_d):
        print("ETH Current Value is: %s. In the last 24h it went up by: %s" % (((str(eth_price_n[0].text).strip()),str(eth_price_24h[0].text).strip())))
    else:
        print("ETH Current Value is: %s. In the last 24h it went down by: %s" % (((str(eth_price_n[0].text).strip()),str(eth_price_24h[0].text).strip())))


btc_grabber()
eth_grabber()
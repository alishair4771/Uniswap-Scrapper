from uniswap_scrapper import Uniswap_scrapper


scraper = Uniswap_scrapper()
scraper.load_uniswap()
scraper.select_pairs()
while True:
    scraper.price()

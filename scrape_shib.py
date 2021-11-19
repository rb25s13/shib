from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    shib_dict = {}

    # get the latest news title and blurb
    homeurl = 'https://coinmarketcap.com/currencies/shiba-inu/'
    browser.visit(homeurl)

    html = browser.html
    soup = bs(html, 'html.parser')

    shib_dict['price'] = soup.find('div', class_='priceValue').text

    # Close the browser after scraping
    browser.quit()

    return shib_dict

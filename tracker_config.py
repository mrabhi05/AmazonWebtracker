from selenium import webdriver

DIRECTORY = 'reports',
NAME = 'ps4',
#CURRENCY = '₹',
MIN_PRICE = '100',
MAX_PRICE = '1000',
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}

BASE_URL = "https://www.amazon.in"

def get_chrome_web_driver(option):
    return webdriver.Chrome('./chromedriver', chrome_options=option)

def get_chrome_web_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(option):
    option.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(option):
    option.add_argument('--incognito')
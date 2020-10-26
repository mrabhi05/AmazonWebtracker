from tracker_config import (
BASE_URL, 
DIRECTORY,
NAME,
#CURRENCY,
FILTERS,
get_chrome_web_driver,
get_chrome_web_options,
set_browser_as_incognito,
set_ignore_certificate_error,


)

class GenerateReport:
    def __init__(self):
        pass


class AmazonAPI:
    def __init__(self, search_term, filters, price, base_url, currency):
        self.base_url = base_url
        self.search_term = search_term
        #self.currency = currency
        option = get_chrome_web_options()
        set_ignore_certificate_error(option)
        set_browser_as_incognito(option)
        self.driver = get_chrome_web_driver(option)
        
        self.price_filter = f"rh=p_36%3A{filter['min']}00-{filter['max']}00"
        
        pass 

    def run(self):
        print("Starting Script.....")
        print(f"Looking for {self.search_term} products")
        links - self.get_products_links()
        
        self.sleep(3)
        self.driver.quit()


    def get_products_links(self):
        self.driver.get(self.base_url)
        element = self.driver.find_element_by_id('twotabsearchtextbox')
        element.send_keys(self.search_term)
        element.send_keys(Keys.ENTER)


if __name__ == '__main__':
    print("Heyy!!")
    amazon = AmazonAPI(NAME, FILTERS, BASE_URL)
    amazon.run()
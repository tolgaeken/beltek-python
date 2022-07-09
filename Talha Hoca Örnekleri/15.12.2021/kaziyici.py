from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Kaziyici:
    def __init__(self, URL):
        self.URL = URL
        self.scraper = webdriver.Chrome(executable_path="/home/talha/Applications/chromedriver/chromedriver")
        

    def _url_ac(self):
        self.scraper.get(self.URL)


class Hepsiburada(Kaziyici):
    def __init__(self, URL):
        super().__init__(URL)
        self._url_temizle()
        

    def _url_temizle(self):
        self.URL = self.URL.split('?')[0]


    def fiyat_getir(self):
        fiyat = None
        self._url_ac()
        try:
            fiyat = self.scraper.find_element(By.CSS_SELECTOR, "span[data-bind=\"text: product().currentListing.currentPriceBeforePoint + ',' + product().currentListing.currentPriceAfterPoint\"]").text
        except NoSuchElementException as nse:
            print("No such element!")
            fiyat = self.scraper.find_element(By.ID, "offering-price").get_attribute("content")
            
        return fiyat

    

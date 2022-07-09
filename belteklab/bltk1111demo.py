from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Kaziyici:
    def __init__(self,URL):
        self.URL = URL
        self.scraper = webdriver.Chrome(executable_path="C:\\Chrome\\chromedriver.exe")
    
    def urlAc(self):
        self.scraper.get(self.URL)
        

class Hepsiburada(Kaziyici):
    def __init__(self,URL):
        super().__init__(URL)

    def urlTemizle(self):
        self.URL = self.URL.split('?')[0]


    def fiyatGetir(self):
        fiyat = None
        self.urlAc()
        try:
            fiyat = self.scraper.find_element(By.CSS_SELECTOR, "span[data-bind=\"text: product().currentListing.currentPriceBeforePoint + ',' + product().currentListing.currentPriceAfterPoint\"]").text
        except NoSuchElementException as nse:
            print("No such element!")
            fiyat = self.scraper.find_element(By.ID, "offering-price").get_attribute("content")
        
        return fiyat

    

class Trendyol(Kaziyici):
    def __init__(self, URL):
        super().__init__(URL)
    
    def fiyatGetir(self):
        fiyat = None
        self.urlAc()
        try:
            fiyat = self.scraper.find_element(By.XPATH,"//*[@id='product-detail-app']/div/div[2]/div[1]/div[2]/div[1]/div/div/div[4]/div[2]/div/span[2]").text
        except NoSuchElementException:
            fiyat = self.scraper.find_element(By.XPATH,"//*[@id='product-detail-app']/div/div[2]/div[1]/div[2]/div[1]/div/div/div[4]/div/div/span").text
        
        return fiyat


class Amazon(Kaziyici):
    def __init__(self, URL):
        super().__init__(URL)
    
    def fiyatGetir(self):
        fiyat = None
        self.urlAc()
        try:
            fiyat = self.scraper.find_element(By.XPATH,"//*[@id='corePrice_desktop']/div/table/tbody/tr[2]/td[2]/span[1]/span[2]").text
        except NoSuchElementException:
            fiyat = self.scraper.find_element(By.XPATH,"//*[@id='corePrice_desktop']/div/table/tbody/tr[1]/td[2]/span[1]/span[2]").text
        return fiyat
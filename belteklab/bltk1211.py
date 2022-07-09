from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")

driver.get("https://www.trendyol.com/liva/tavuk-etli-kedi-mamasi-15-kg-p-32718068?boutiqueId=61&merchantId=185267")
try:
    result = driver.find_element(By.XPATH,"//*[@id='product-detail-app']/div/div[2]/div[1]/div[2]/div[1]/div/div/div[4]/div[2]/div/span[2]").text
except NoSuchElementException:
    result = driver.find_element(By.XPATH,"//*[@id='product-detail-app']/div/div[2]/div[1]/div[2]/div[1]/div/div/div[4]/div/div/span").text

print(result)
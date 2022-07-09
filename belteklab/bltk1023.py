from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Tolga\\AppData\\Local\\SeleniumBasic\\chromedriver.exe")
driver.get("https://www.amazon.com.tr/")

arama = driver.find_element(By.LINK_TEXT,"Giriş yap")
# arama = driver.find_element(By.XPATH,"//*[@id=\"auto-complete-app\"]/div/div/input")
arama.click()

email = driver.find_element(By.NAME,"email")
email.send_keys("a@a.com")


a = input()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.trendyol.com/")

arama = driver.find_element(By.XPATH,"//*[@id='auto-complete-app']/div/div/input")
# arama = driver.find_element(By.XPATH,"//*[@id=\"auto-complete-app\"]/div/div/input")
arama.send_keys("Kedi Maması")
arama.send_keys(Keys.RETURN)

a = input()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Chrome\\chromedriver.exe")
driver.get("https://www.hepsiburada.com/ara?q=HBV00001AYD3B")

# arama = driver.find_element(By.XPATH,"//*[@id='SearchBoxOld']/div/div/div[1]/div[2]/input")
# arama.send_keys("Kedi Maması")
# arama.send_keys(Keys.RETURN)


liste = driver.find_element(By.XPATH,"//*[@id='i0']/div/a/div[2]/div[1]/div/picture/img").src
# for i in liste:
#     urun = driver.find_element(By.ID,"i"+ str(i))

print(liste)

a = input()
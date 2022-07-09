from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("--headless")
# chromeOptions.add_argument("--no-sandbox")
# chromeOptions.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")

driver.get("https://www.google.com")

arama = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
arama.send_keys("Beltek")
arama.send_keys(Keys.RETURN)

test = input()
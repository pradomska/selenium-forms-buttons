from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=webdriver.ChromeOptions())
driver.maximize_window()
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "View source")
all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()

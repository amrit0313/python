from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# articles.click()
print(articles.text)
wiki = driver.find_element(By.LINK_TEXT, "Wikipedia")
# wiki.click()
time.sleep(5)
# maximize the screen
search_box = driver.find_element(By.NAME, "search")
text = "python"
search_box.send_keys(text)
search_box.send_keys(Keys.ENTER)
input()

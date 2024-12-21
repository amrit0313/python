from selenium import webdriver
from selenium.webdriver.common.by import By

dict = {}
i = 0

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

title = driver.find_elements(By.XPATH, "//*[@id='content']/div/section/div[3]/div[2]/div/ul/li")
for date in title:
    dat = date.text
    new = dat.splitlines()
    dict[i]={
        "date":new[0],
        "name":new[1]
    }
    i+=1

print(dict)

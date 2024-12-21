from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.amazon.com/Turtle-Gaming-Headset-PlayStation-Nintendo-Console/dp/B00YXO5U40/ref=sr_1_1?_encoding=UTF8&sr=8-1")
title = driver.title
driver.implicitly_wait(0.5)

select_by_id = driver.find_element(By.ID, "productTitle")
print(select_by_id.text)

select_by_class = driver.find_elements(By.CLASS_NAME, "a-spacing-mini")
for item in select_by_class:
    print(item.text)
specifications = driver.find_elements(By.CSS_SELECTOR, ".a-span9  span")
for specification in specifications:
    print(specification.text)


#if all these selectors dont work, we can use xpath, we can drill from tags to tags
select_by_xpath = driver.find_element(By.XPATH, "//*[@id='productOverview_feature_div']/div/table/tbody/tr[4]/td[2]/span")
#note:we can directly copy xpath from the browser, using right click on tags on inspect
print(select_by_xpath.text)
driver.quit()
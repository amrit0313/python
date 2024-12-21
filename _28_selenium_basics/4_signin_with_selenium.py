from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://amrtzshop.netlify.app")  # the link you want to be on
login_button = driver.find_element(By.CLASS_NAME, "header_login__j3a8U")
login_button.click()
time.sleep(2)
email_input = driver.find_element(By.XPATH, "//*[@id='email']")
email_input.send_keys("you mail")
password_input = driver.find_element(By.XPATH, "//*[@id='password']")
password_input.send_keys("password")
password_input.send_keys(Keys.ENTER)
input()

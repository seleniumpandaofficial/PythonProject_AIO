from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")
title_HomePage = driver.title
print(title_HomePage)
currentURL_HomePage = driver.current_url
print(currentURL_HomePage)

driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Register").click()

title_RegisterPage = driver.title
print(title_RegisterPage)
currentURL_RegisterPage = driver.current_url
print(currentURL_RegisterPage)

driver.quit()
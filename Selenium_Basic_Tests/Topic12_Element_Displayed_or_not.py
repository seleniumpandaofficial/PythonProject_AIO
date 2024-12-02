import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")

MyAccountLink = driver.find_element(By.LINK_TEXT, "My Account")
print(MyAccountLink.is_displayed())

if MyAccountLink.is_displayed():
    time.sleep(2)
    MyAccountLink.click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Login").click()
else:
    print("Not Displayed")


driver.quit()
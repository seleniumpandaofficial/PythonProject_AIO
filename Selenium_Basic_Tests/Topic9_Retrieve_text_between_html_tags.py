import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium_Basic_Tests.Topic7_Identifying_Element_Separately import MyAccountLink

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")

My_AccountLink = driver.find_element(By.LINK_TEXT, "My Account").text
time.sleep(5)
print(My_AccountLink)



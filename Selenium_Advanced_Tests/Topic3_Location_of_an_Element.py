from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")

MyAccountLink = driver.find_element(By.LINK_TEXT, "My Account").location

print(MyAccountLink.get("x"))
print(MyAccountLink.get("y"))

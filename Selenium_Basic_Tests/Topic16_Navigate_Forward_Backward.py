from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Login").click()

LoginPageTitle = driver.title
print(LoginPageTitle)

driver.back()


print(driver.title)

driver.forward()
print(driver.title)
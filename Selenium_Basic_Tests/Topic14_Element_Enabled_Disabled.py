from wsgiref.simple_server import demo_app

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")

HomePageTitle = driver.title
print(HomePageTitle)
HomePageCurrentURL = driver.current_url
print(HomePageCurrentURL)

MyAccountLink = driver.find_element(By.LINK_TEXT, "My Account")

if MyAccountLink.is_enabled():
    MyAccountLink.click()
else:
    print("Link is not enabled")

LoginLink = driver.find_element(By.LINK_TEXT, "Login")

if LoginLink.is_enabled():
    LoginLink.click()
else:
    print("Loging link is not enabled")

driver.find_element(By.ID, "input-email").send_keys("seleniumpanda@gmail.com")
driver.find_element(By.ID, "input-email").clear()
driver.find_element(By.ID, "input-email").send_keys("seleniumpanda@gmail.com")

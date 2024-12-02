from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")

MyAccountLink = driver.find_element(By.LINK_TEXT, "My Account")
MyAccountLink.click()

LoginLink = driver.find_element(By.LINK_TEXT, "Login")
LoginLink.click()

emailTextBox = driver.find_element(By.ID, "input-email")
emailTextBox.send_keys("seleniumpanda@gmail.com")

passwordTextBox = driver.find_element(By.ID, "input-password")
passwordTextBox.send_keys("Selenium@123")

loginButton = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")
loginButton.click()

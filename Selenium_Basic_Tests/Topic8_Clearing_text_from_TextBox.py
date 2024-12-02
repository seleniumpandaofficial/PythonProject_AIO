import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Login").click()

emailTextBox = driver.find_element(By.ID, "input-email")
time.sleep(1)
emailTextBox.send_keys("seleniumpanda@gmail.com")
time.sleep(1)
emailTextBox.clear()
time.sleep(1)
emailTextBox.send_keys("seleniumpanda@gmail.com")

time.sleep(1)
passwordTextBox = driver.find_element(By.ID, "input-password")
time.sleep(1)
passwordTextBox.send_keys("Selenium@123")
time.sleep(1)
passwordTextBox.clear()
time.sleep(1)
passwordTextBox.send_keys("Selenium@123")

driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
time.sleep(1)

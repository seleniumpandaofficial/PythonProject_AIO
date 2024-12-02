from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(2)
driver.get("https://tutorialsninja.com/demo")
from selenium import webdriver

options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.google.com/")+
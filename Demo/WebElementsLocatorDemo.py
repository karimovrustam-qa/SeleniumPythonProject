from selenium import webdriver

driver = webdriver.Chrome("../Drivers/chromedriver")

driver.get("https://google.com")

searchBox = driver.find_element_by_name("q")
searchBox.send_keys("Rustam")

driver.close()
driver.quit()
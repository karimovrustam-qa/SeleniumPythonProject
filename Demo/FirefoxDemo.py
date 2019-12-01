from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")

path = "../Drivers/geckodriver"
driver = webdriver.Firefox(executable_path=path, firefox_options=firefox_options)

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_id("gsr").send_keys(Keys.ENTER)

time.sleep(2)
print(driver.title)

driver.close()
driver.quit()
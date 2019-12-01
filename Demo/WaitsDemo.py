from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
# Implicit Waits
# driver.implicitly_wait(10)

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation")
wait = WebDriverWait(driver,10)
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
    print("element is clickable")
except:
    print("element is not clickable")
    exit(1)
element.click()
# driver.find_element_by_name("btnK").click()
print("Test completed")
driver.close()
driver.quit()
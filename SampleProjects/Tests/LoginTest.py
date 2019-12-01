from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import sys # for running with terminal (ADD BEFORE external FOLDERS, for example "SampleProjects")
import os # for running with terminal (ADD BEFORE external FOLDERS, for example "SampleProjects")
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..")) # for running with terminal (ADD BEFORE external FOLDERS, for example "SampleProjects")
from SampleProjects.Pages.LoginPage import LoginPage
from SampleProjects.Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../../Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        homepage.click_logout_link()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/karimovrustam/PycharmProjects/Selenium/Reports"))
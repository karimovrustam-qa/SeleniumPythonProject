from SampleProjects.Locators.Locators import Locators
class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome_link(self):
        self.driver.find_element_by_id(Locators.welcome_link_id).click()

    def click_logout_link(self):
        self.driver.find_element_by_link_text(Locators.logout_link_linkText).click()
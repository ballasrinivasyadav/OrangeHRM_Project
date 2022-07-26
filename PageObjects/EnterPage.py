from selenium.webdriver.common.by import By


class EnterPage:

    def __init__(self,driver):
        self.driver = driver

    enter = (By.ID,"country")

    def enterItem(self):
        return self.driver.find_element(*EnterPage.enter)
#self.driver.find_element_by_id("country").send_keys("ind")

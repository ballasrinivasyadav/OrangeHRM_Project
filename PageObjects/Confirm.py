from selenium.webdriver.common.by import By


class Confirm:

    def __init__(self,driver):
        self.driver = driver
    confirm =(By.XPATH,"//input[@type='submit']")
    successful = (By.CLASS_NAME,"alert-success")
#self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    def getConfirm(self):
        return self.driver.find_element(*Confirm.confirm)

#self.driver.find_element_by_class_name("alert-success")
    def getSuccessful(self):
        return self.driver.find_element(*Confirm.successful)

from selenium.webdriver.common.by import By

class CheckOut:
    def __init__(self,driver):
        self.driver = driver
    products = (By.XPATH,"//div[@class='card h-100']")
    checkoutitem = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkoutbutton = (By.CSS_SELECTOR,"[class*='btn btn-success']")
    checkbox = (By.XPATH,"//label[@for='checkbox2']")
    # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    def getaddItems(self):
          return self.driver.find_elements(*CheckOut.products)

    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    def getcheckOutItem(self):
        return self.driver.find_element(*CheckOut.checkoutitem)

    # self.driver.find_element_by_css_selector("[class*='btn btn-success']").click()
    def getcheckOutbutton(self):
        return self.driver.find_element(*CheckOut.checkoutbutton)

    #self.driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
    def getCheckBox(self):
        return self.driver.find_element(*CheckOut.checkbox)




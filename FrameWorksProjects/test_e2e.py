import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from FramesWorks.BaseClass import BaseClass
from PageObjects.Checkout import CheckOut
from PageObjects.Confirm import Confirm
from PageObjects.EnterPage import EnterPage
from PageObjects.HomePage import HomePage


@pytest.mark.usefixtures

class Test_FirstClass(BaseClass):
    def test_One(self,setup):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
            #self.driver.find_element_by_css_selector("a[href*='shop']").click()

        #products = CheckOut.getaddItems()
        #products.getaddItems()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                    product.find_element_by_xpath("div/button").click()
            checkoutitem = CheckOut(self.driver)
            checkoutitem.getcheckOutItem().click()
            #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
            checkoutbutton = CheckOut(self.driver)
            checkoutbutton.getcheckOutbutton().click()
            #self.driver.find_element_by_css_selector("[class*='btn btn-success']").click()

#driver.find_element(By.XPATH,"//button[@class='btn btn-success']").clcik()
            enter_item = EnterPage(self.driver)
            enter_item.enterItem().send_keys("ind")
            #self.driver.find_element_by_id("country").send_keys("ind")
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"app-checkout[class='row'] ul:nth-child(1) li:nth-child(1) a:nth-child(1)"))).click()

            #self.driver.find_element_by_xpath("//a[normalize-space()='India']").clcik()
            log = self.getlogger()
            log.info("getting all the card titles")
            checkboxitem = CheckOut(self.driver)
            checkboxitem.getCheckBox().click()
            #self.driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
            log.debug("getting all the cofirmitem")
            confirmitem = Confirm(self.driver)
            confirmitem.getConfirm().click()
            #self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
            successText = Confirm(self.driver)
            successText.getSuccessful().text()
            print(successText)
            #successText = self.driver.find_element_by_class_name("alert-success").text
            assert "Success! Thank you!" in successText
            self.driver.get_screenshot_as_file("screen.png")


import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import  webdriver


@pytest.mark.usefixture("setup")
class Test_Orange():

    def test_Orange(self):

        self.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_css_selector("[class*='button']").click()

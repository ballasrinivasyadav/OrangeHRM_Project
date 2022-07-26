import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from FrameWorksProjects.conftest import setup

#@pytest.mark.usefixture("setup")
from FramesWorks.BaseClass import BaseClass
class Test_e2e:
        def __init__(self,driver):
                self.driver = driver
        def test_One(self):
                driver = webdriver.Chrome(executable_path="C:\\Users\\Srinivas\\PycharmProjects\\Udemy\\Selenium\\Drivers")
                driver.get("https://rahulshettyacademy.com/angularpractice/")
                self.driver.maximize_window()
                self.driver.find_element_by_name("name").send_keys("Srinivas")
                self.driver.find_element(By.CSS_SELECTOR,"input[name*='email']").send_keys("Srinivas@123")
                self.driver.find_element(By.CSS_SELECTOR,"input[id*='exampleInputPassword1']").send_keys("Admin123")
                self.driver.find_element(By.CSS_SELECTOR,"input[id*='exampleCheck1']").click()
                sel = Select(self.driver.find_element(By.ID,"exampleFormControlSelect1"))
                sel.select_by_visible_text("Male")
                self.driver.find_element(By.ID,"inlineRadio1").clcik()
                self.driver.find_element(By.CSS_SELECTOR,"input[class*='btn btn-success']").click()
                alertText = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert alert-success alert-dismissible']").text
                assert("Success!" in alertText)
                print(alertText)

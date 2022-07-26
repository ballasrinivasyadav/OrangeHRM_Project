import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("Browser_name",action="store",default="chrome")
@pytest.fixture
def setup(request, driver):
    browser = driver.request.config.getoption("Browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path="C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//geckodriver.exe")
    else:
        print("Ie")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

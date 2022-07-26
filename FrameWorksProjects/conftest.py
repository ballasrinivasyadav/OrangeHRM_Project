import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#def pytest_addoption(parser):
#    parser.addoption("--browser_name", action="store", default="chrome")
@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome(executable_path="C:\\Users\\Srinivas\\PycharmProjects\\Udemy\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
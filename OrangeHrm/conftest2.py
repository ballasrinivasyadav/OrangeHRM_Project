import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption("Browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Srinivas\\PycharmProjects\\Udemy\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver

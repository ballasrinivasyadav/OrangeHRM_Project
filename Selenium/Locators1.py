from datetime import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C://Users//Srinivas//PycharmProjects//Udemy\Selenium//Drivers//chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.maximize_window()
driver.find_element_by_css_selector("#username").send_keys("Shetty")
driver.find_element_by_css_selector(".password").send_keys("Sweety")
driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_link_text("Forgot Your Password?").click()

driver.find_element_by_xpath("//input[@name='cancel']").click()
dropdown = select(driver.find_elements_by_id())
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)

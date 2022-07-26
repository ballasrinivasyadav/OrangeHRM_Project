from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("a[href*='shop']").click()
Products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in Products:
     productName = product.find_element_by_xpath("div/h4/a").text
     if productName == "Blackberry":
         product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector("[class*='btn btn-success']").clcik()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located(By.XPATH,"//a[normalize-space()='India']"))).click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
sucessText = driver.find_elements_by_css_selector("alert-success").text
assert "Success! Thank You!" in sucessText
driver.get_screenshot_as_file("screen.png")
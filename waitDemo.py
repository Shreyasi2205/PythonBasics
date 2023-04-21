from unittest import result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

results = driver.find_elements(By.XPATH,"//div[@class='products'] /div/div/button")
count = len(results)
assert count>0
for result in results:
    result.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='cart-preview active'] button[type='button']").click()

# implicit wait - if any element dosen't show up on the page it will wait for maximum the given
# seconds to show up 
driver.implicitly_wait(5)

# explicit wait
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,"promocode").text)
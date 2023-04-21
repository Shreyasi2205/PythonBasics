import time
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# it the search function will take time to search ind so we put sleep
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
# it might be the case that india appears at diff positions so we have to scan all the options
# it will identify all elements in page
coun = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
email=driver.find_element(By.XPATH,"//input[@id='edit-name']")
print(len(coun))
for country in coun:
    if country.text == "India":
        country.click()
        break
# print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
# used when there is dynamic test is used
assert driver.find_element(By.ID,"autosuggest").get_attribute("value")== "bIndia"
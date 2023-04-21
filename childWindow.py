import imp
from time import sleep
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT,"A/B Testing").click()

# this will not work as this opens in different page
# provide window name

# it will create a list of all the windows that are opened
windowsOpend= driver.window_handles
print(len(windowsOpend))
driver.switch_to.window(windowsOpend[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
#driver.switch_to.default_content()
#driver.switch_to.window(windowsOpend[1])
# print(driver.find_element(By.TAG_NAME,"h3").text)
sleep(20)


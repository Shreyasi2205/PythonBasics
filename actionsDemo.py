import imp
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# there is class called ActionChains
action= ActionChains(driver) # send driver as an argument
# if you want to long press
# action.click_and_hold()
# # if you want to right click
# action.context_click()
# # double clicl
# action.double_click()
# action.drag_and_drop()

# whenever you perform any action using action method we need to add .perform to 
# finish that action
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
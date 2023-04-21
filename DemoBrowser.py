from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pytest

serviceObj= Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver") # create service object that you have to send as property
#to the chrome class
# chrome dirver we need to invoke it to start the browser
driver=webdriver.Chrome(service=serviceObj)  # inside chrome import service
# to maximize the window
driver.maximize_window()
driver.get("https://www.python.org")
print(driver.title)  # Welcome to Python.org 
# property -> don't give brackets and methods -> give brackets

# want to go inside any of the main page
driver.get("https://www.python.org/psf-landing/")
driver.minimize_window()

# to make sure we landed in the correct url
print(driver.current_url)  # https://www.python.org/
driver.refresh() # refresh the page
driver.forward()
# goes to previous page
driver.back()
driver.close()


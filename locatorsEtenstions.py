from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.get("https://rahulshettyacademy.com/client/")

# 1. Check whether 'forget password' is a link'
# here we will use the Text of that link
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# there is partial link text also

#driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()

# we can also go from parent tag to child tag in Xpath
# //form/div[1]/input (now there are many divs so by giving div[1] we are saying we want to go to the first div)

# fill the email box
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("shreyasi22knp@gmail.com")
# driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("123456")

# to write CSS selector in a similar way for div:nth-child() input
# so password will be form div:nth-child(2) input
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("123456")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# you can also check with text in Xpath
# driver.find_element(By.XPATH,"//button[@text='Save new Password']").click()
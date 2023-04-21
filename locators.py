from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# now we have to check email box in this page and type your email

# id, name, Xpath, CSS selector, classname, linkRext
driver.find_element(By.NAME,"email").send_keys("shreyasi22knp@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Shreyasi Sinha")

# static dropdown

# there is a class Select where you have to give the dropdown location
dropDown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# when two option comes first one is at the 0 index and second one is at the 1st index
dropDown.select_by_index(1)
# you can also select based on the given text
#dropDown.select_by_visible_text("Female")

# for gender student type radio option
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
# or other method is #id and .classname
#driver.find_element(By.CSS_SELECTOR,".inlineRadioOptions").click()
# for Xpath we need to write -> //tagname[@attribute='value']
# for submit //tagname[@attribute='value] -> //input[@type='submit]

# [3] shows the third box
driver.find_element(By.XPATH,"//input[@type='submit']").click()

# after clicking on the submit want to check success message is coming or not
# <div class="alert alert-success alert-dismissible"> whenever we see spaces in class
# it means that they are three different class so you can take any class
# text will grap the text in that class
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
# we will use assertion to see if the message is correct or not
assert "Success" in message
# CSS selector -> typename[attribute='value'] or #id or .classname
                  
# [3] shows the third box
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello again")
# if you want to clear everything
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
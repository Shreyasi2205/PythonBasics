from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Shreyasi")
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()

# now when the alert shows the browser doesn't know alert so we haveto switch from
# driver mode to alert mode
alert = driver.switch_to.alert
alertText=alert.text
print(alertText) #Hello Shreyasi, share this practice page and share your knowledge
# to click ok on alert we do .accept
assert "Shreyasi" in alertText
alert.accept()
# or to cancel we use -> alert.dismiss()

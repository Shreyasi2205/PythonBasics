from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

serviceObj=Service("/Users/sinhash8/Documents/PythonBasics/driver/chromedriver")
driver=webdriver.Chrome(service=serviceObj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.find_element(By.ID,"checkBoxOption1").click()

checkboxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("name") == "checkBoxOption1":
        checkbox.click()
        # to check if it is checked
        assert checkbox.is_selected()
        break

driver.find_element(By.XPATH,"//input[@class='inputs ui-autocomplete-input']").send_keys("123455")

# Drop down 
dropdown= Select(driver.find_element(By.ID,"dropdown-class-example"))
# dropdown.select_by_index(2)
dropdown.select_by_value("option3")


# Radio Button Example
radio_buttons= driver.find_elements(By.XPATH,"//input[@class='radioButton']")
print(len(radio_buttons))
for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected() == True
        break
# hide the text
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.XPATH,"//input[@value='Hide']").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
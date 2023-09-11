import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as p

driver = webdriver.Chrome()
driver.get('https://entrar.in/login/login')
usrnm = 'usrnm'          
pswd = 'pswd'
time.sleep(5)

# Simulate login
driver.find_element(By.NAME, 'username').send_keys(usrnm)
driver.find_element(By.NAME, 'password').send_keys(pswd)
driver.find_element(By.NAME, 'password').submit()

# Simulate tab presses using JavaScript
for _ in range(21):
    p.press('tab')

# Simulate enter press using JavaScript
p.press('enter')

# Set a start time for the timeout
start_time = time.time()

while time.time() - start_time < 600:  # Continue for up to 10 minutes (600 seconds)
    try:
        element = driver.find_element(By.XPATH, "//a[@class='tabledit-edit-button btn btn-success waves-effect waves-light'][@target='_blank'][text()='Join']")
        if element:
            element.click()
            print("Element found and clicked.")
            # Reset the start time since the element was found
            start_time = time.time()
        else:
            print("Element not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Close the WebDriver
driver.quit()

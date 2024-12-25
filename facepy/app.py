from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


driver_path = "C:\\Users\\msı\\Desktop\\afdsff\\driver\\chromedriver.exe"
service = Service(driver_path)


driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.facebook.com")

    time.sleep(2)

    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("temurhakanberke@gmail.com")  

    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys("Erzincan123456")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    time.sleep(20000)

except Exception as e:
    print(f"Hata oluştu: {e}")

finally:
    driver.quit()
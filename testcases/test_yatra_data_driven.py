import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#this code is not working as expected because the xpath is not working properly
# @ddt
# @dat
@pytest.mark.parametrize("email, mobile, password, title_card, fname, lname", (["addalasaicse2019@gmail.com", "8247853855", "A868850@s", "Mr", "Sai venkatesh", "Addala"], ["saivenkateshaddala@gmail.com", "9030831377", "A868850@s", "Mr", "Sai venkatesh", "Addala"]))
def test_yatra(email, mobile, password, title_card, fname, lname):
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//span[contains(text(),'Login / Signup')]").click()
    driver.find_element(By.XPATH, "//p[normalize-space()='Login or Create Account']").click()
    Email=driver.find_element(By.XPATH, "//input[@id='login-input']")
    Email.click()
    Email.send_keys(email)
    
    Continue=driver.find_element(By.ID,"login-continue-btn")
    Continue.click()

    Mobile_number=driver.find_element(By.ID, "signup-mobile-number")
    Mobile_number.click()
    Mobile_number.send_keys(mobile)

    Create_password=driver.find_element(By.ID, "signup-password")
    Create_password.click()
    Create_password.send_keys(password)

    Title=driver.find_element(By.ID, "signup-user-designation")
    Title.click()
    Title.send_keys(title_card)

    First_name=driver.find_element(By.ID, "signup-user-first-name")
    First_name.click()
    First_name.send_keys(fname)

    Last_name=driver.find_element(By.ID, "signup-user-last-name")
    Last_name.click()
    Last_name.send_keys(lname)

    Spaecial_promotions=driver.find_element(By.XPATH, "//label[@for='specialPromoNotif']")
    Spaecial_promotions.click()

    Whatapp_notifiacations=driver.find_element(By.XPATH, "//label[@for='whatsAppNotif']")
    Whatapp_notifiacations.click()

    Create_Account=driver.find_element(By.ID, "signup-form-continue-btn")
    Create_Account.click()      

    time.sleep(5)
    
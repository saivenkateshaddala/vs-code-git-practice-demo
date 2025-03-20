import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import openpyxl


def load_excel_data():
    workbook = openpyxl.load_workbook(r"C:\Users\Devarapu Ganesh\Downloads\yatradata.xlsx")
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
        data.append({
            "email": row[0],
            "mobile": row[1],
            "password": row[2],
            "title_card": row[3],
            "fname": row[4],
            "lname": row[5]
        })
    return data

@pytest.mark.parametrize("data", load_excel_data())
def test_yatra(data):
    email = data["email"]
    mobile = data["mobile"]
    password = data["password"]
    title_card = data["title_card"]
    fname = data["fname"]
    lname = data["lname"]
    
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
    
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SubscriberADD():
    def __init__(self, driver):
        self.driver = driver
        

    # locators
    Manage_Subscribers = "//button[normalize-space()='Manage Subscribers']"
    Add_Subscriber = "//span[normalize-space()='Add Subscribers']"
    Upload_CSV = "//span[normalize-space()='Upload CSV']"
    file_upload = "//input[@type='file']"
    Save_and_Add_Subscribers = "//button[normalize-space()='Save and Add Subscribers']"

    def Manage_Subscribers_button(self):
        self.driver.find_element(By.XPATH, self.Manage_Subscribers).click()
    
    def Add_Subscribers_button(self):
        self.driver.find_element(By.XPATH, self.Add_Subscriber).click()

    def Upload_CSV_button(self):
        self.driver.find_element(By.XPATH, self.Upload_CSV).click()

    def file_upload_button(self, file_path):
        self.driver.find_element(By.XPATH, self.file_upload).send_keys(file_path)

    def Save_and_Add_Subscribers_button(self):
        self.driver.find_element(By.XPATH, self.Save_and_Add_Subscribers).click()
    

    def Add_Subscribers(self,file_path):
        self.Manage_Subscribers_button()
        self.Add_Subscribers_button()
        self.Upload_CSV_button()
        self.file_upload_button(file_path)
        time.sleep(4)
        self.Save_and_Add_Subscribers_button()
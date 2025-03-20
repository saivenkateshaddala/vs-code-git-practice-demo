from selenium.webdriver.common.by import By
import time

class NetworkSelect():
    def __init__(self,driver):
        self.driver= driver

    #locators
    MasterNet="//button[normalize-space()='Network: masternet']"
    VMGW="//span[normalize-space()='vm-gw']"
    Dashboard_selectors=".jss58.jss59"
    Subscribers="//a[@href='/nms/vm-gw/subscribers']"
    dot_button="//tbody/tr[2]/td[7]/div[1]/button[1]//*[name()='svg']"
    remove_button="//li[normalize-space()='Remove']"
    confirm_button="//button[normalize-space()='Confirm']"

    def Network_masternet(self):
        self.driver.find_element(By.XPATH, self.MasterNet).click()

    def VMGW_selector(self):
        self.driver.find_element(By.XPATH, self.VMGW).click()

    def Dashboard_selector(self):
        self.driver.find_element(By.CSS_SELECTOR, self.Dashboard_selectors).click()

    def Subscribers_button(self):
        self.driver.find_element(By.XPATH, self.Subscribers).click()   

    def dot_button_click(self):
        self.driver.find_element(By.XPATH, self.dot_button).click()
    
    def remove_button_click(self):
        self.driver.find_element(By.XPATH, self.remove_button).click()
    
    def confirm_button_click(self):
        self.driver.find_element(By.XPATH, self.confirm_button).click()

     

    def Network_select(self):
        self.Network_masternet()
        time.sleep(2)
        self.VMGW_selector()
        self.Dashboard_selector()
        self.Subscribers_button()
        time.sleep(4)
        self.dot_button_click()
        time.sleep(4)
        self.remove_button_click()
        time.sleep(4)
        self.confirm_button_click()

       
        
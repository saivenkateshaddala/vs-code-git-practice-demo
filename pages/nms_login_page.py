from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage():
    def __init__(self,driver):
        self.driver= driver


    #locator
    details_bitton="//button[@id='details-button']"
    proceed_link="//a[@id='proceed-link']"
    email="//input[@name='email']"
    password="password"



    def details_button_click(self):
        self.driver.find_element(By.XPATH, self.details_bitton).click()

    def proceed_link_click(self):
        self.driver.find_element(By.XPATH, self.proceed_link).click()

    def enter_email(self):
        return self.driver.find_element(By.XPATH, self.email)
        
    def enter_password(self):
        return self.driver.find_element(By.NAME, self.password)

    def click_login_button(self):
        return self.driver.find_element(By.XPATH, self.login_button)
        

    def email_id(self,email):
        en=self.enter_email()
        en.click()
        en.send_keys(email)

        
    def password_id(self,password):
        self.enter_password().click()
        self.enter_password().send_keys(password)
        self.enter_password().send_keys(Keys.ENTER)


    def details(self,email,password):
        self.details_button_click()
        self.proceed_link_click()
        self.email_id(email)
        self.password_id(password)




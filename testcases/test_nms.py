
import pytest
import json
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.nms_login_page import LoginPage
from pages.network_select import NetworkSelect
from pages.subscriber_add_page import SubscriberADD

logging.basicConfig(
    level=logging.DEBUG,
    filename="testnms1.log",
    format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p"
)

@pytest.mark.usefixtures("setup")   
class TestNMS:
# Load data from JSON file
    def load_test_data():
        with open("C:\\vscode_with_selenium\\testdata\\testdata.json", "r") as file:
            return json.load(file)

# Parameterize test cases using loaded JSON data
    @pytest.mark.parametrize("credentials", load_test_data())
    def test_nms(self,credentials):
        email = credentials["email"]
        password = credentials["password"]
        wait = WebDriverWait(self.driver, 10)
        file_path = r"C:\\Users\\Devarapu Ganesh\\Downloads\\subscribers_1738058399343.csv"
        self.driver.get("https://wavelabs.nms.pmn-dev.wavelabs.in/")
        self.driver.maximize_window()
        
        # Login to NMS
        NLP=LoginPage(self.driver)
        NLP.details(email,password)

        # Select Network and navigate to Subscribers    
        NS=NetworkSelect(self.driver)
        NS.Network_select()
        time.sleep(4)

        # Add Subscribers
        SA=SubscriberADD(self.driver)
        SA.Add_Subscribers(file_path)
        time.sleep(4)

        logging.warning("Subscriber added successfully")
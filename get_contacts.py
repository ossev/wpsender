# from datetime import time
from os import get_inheritable
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\osnas\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

class HomePageTests(unittest.TestCase):

    def setUp(self) -> None:
        
        # self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        pathChromeDriver = 'C:/Users/osnas/Documents/scripts_python/wpsender/chromedriver.exe'
        s = Service(pathChromeDriver)
        
        options = webdriver.ChromeOptions()
        options.add_argument(CHROME_PROFILE_PATH)
        self.driver = webdriver.Chrome(service=s,options=options)
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_getMsgInterface(self):
        # contact_errors = pd.DataFrame(columns=["celular"])

        # contact_names = ['Daniel Lesmes','Humbewrewassfd','Fabio Sarmiento']
        # Obtener el input donde se ingresa el número de contacto para buscar el chat
        searchBox = '//*[@id="side"]/div[1]/div/label/div/div[2]'

        # inputSearch = self.driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]')

        noEnviados = []
        data = pd.read_excel("Data.xlsx")
        viajes = pd.read_excel("Viajes.xlsx")
        filepath = 'C:/Users/osnas/Documents/scripts_python/wpsender/images/cargas.jpg'
        text_msg = 'Para más información ingresa al siguiente link: https://wa.me/573008825313'

        wait = WebDriverWait(self.driver,5)
        inputSearch = wait.until(lambda driver:self.driver.find_element(By.XPATH,searchBox))
        inputSearch.send_keys("TC")

        time.sleep(10)

        contacts_class = "_2nY6U"
        contacts = wait.until(lambda driver:self.driver.find_elements(By.CLASS_NAME,contacts_class))
        print(len(contacts))
        # for contact in contacts:
        #     name = contact.find_element(By.XPATH,'.//span[@dir="auto"]').text
        #     print(name)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
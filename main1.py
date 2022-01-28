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

        data = pd.read_excel("Data.xlsx")
        viajes = pd.read_excel("Viajes.xlsx")

        for index, row in data.iterrows():
            contact_name = row['contact_name']

            try:
                # Esperar a que cargue la página, máximo por 15 segundos
                # Asegurarse de que está limpio el input
                wait = WebDriverWait(self.driver,30)
                inputSearch = wait.until(lambda driver:self.driver.find_element(By.XPATH,searchBox))

                inputSearch.clear()

                # ingresar el número de contacto
                inputSearch.send_keys(contact_name)

                contact_xpath = '//span[@title="{}"]'.format(contact_name)


                # contact_xpath = '//*[@id="pane-side"]/div[1]/div/div/div[7]'

                # inputSearch = wait.until(lambda driver:self.driver.find_element(By.XPATH,searchBox))
                # contact_title = self.driver.find_element(By.XPATH,contact_xpath)
                contact_title = wait.until(lambda driver:self.driver.find_element(By.XPATH,contact_xpath))
                contact_title.click()

                inputMessage_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
                inputMessage = wait.until(lambda driver:self.driver.find_element(By.XPATH,inputMessage_xpath))

                # mensaje = row['message']
                # inputMessage.send_keys(mensaje)

                for index2, row2 in viajes.iterrows():
                    msg = '*Tipo de vehículo*: {}'.format(row2['tipo_vehiculo'])
                    inputMessage.send_keys(msg)
                    inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    msg = '*Origen*: {}'.format(row2['origen'])
                    inputMessage.send_keys(msg)
                    inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    msg = '*Destino*: {}'.format(row2['destino'])
                    inputMessage.send_keys(msg)
                    inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    msg = '*Carrocería*: {}'.format(row2['carroceria'])
                    inputMessage.send_keys(msg)
                    inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    msg = '*Flete*: {}'.format(row2['flete'])
                    inputMessage.send_keys(msg)
                    inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    msg = '*Observaciones*: {}'.format(row2['observaciones'])
                    inputMessage.send_keys(msg)
                    inputMessage.send_keys(Keys.ENTER)
                    
                # inputMessage.send_keys(Keys.ENTER)

            except:
                error_msg = "No se puedo enviar el mensaje a: {}".format(contact_name)
                print(error_msg)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
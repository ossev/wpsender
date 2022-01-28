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

        phones = ['Rosa Quintero','Mom']
            # Obtener el input donde se ingresa el número de contacto para buscar el chat
        searchBox = '//*[@id="side"]/div[1]/div/label/div/div[2]'

        # inputSearch = self.driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]')

        for phone in phones: 
            # Esperar a que cargue la página, máximo por 15 segundos
            # Asegurarse de que está limpio el input
            wait = WebDriverWait(self.driver,30)
            inputSearch = wait.until(lambda driver:self.driver.find_element(By.XPATH,searchBox))

            inputSearch.clear()

            # ingresar el número de contacto
            inputSearch.send_keys(phone)

            contact_xpath = '//span[@title="{phone}"]'


            # contact_xpath = '//*[@id="pane-side"]/div[1]/div/div/div[7]'

            # inputSearch = wait.until(lambda driver:self.driver.find_element(By.XPATH,searchBox))
            # contact_title = self.driver.find_element(By.XPATH,contact_xpath)
            contact_title = wait.until(lambda driver:self.driver.find_element(By.XPATH,contact_xpath))
            contact_title.click()

            inputMessage_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
            inputSearch = wait.until(lambda driver:self.driver.find_element(By.XPATH,inputMessage_xpath))

            mensaje = '*Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Bogota, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Bogota, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Tractomula, *Tipo de Carrocería*: Furgon, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Estacas, *Origen*: Bogota, *Destino*: Barranquilla, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Barranquilla, *Destino*: Itagui, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Itagui, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Valle, *Destino*: Bogota, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234 \n *Tipo de vehiculo*: Sencillo, *Tipo de Carrocería*: Furgon, *Origen*: Bogota, *Destino*: Valle, *Observaciones*: Obs dfa fds dsdfs sdf esgd sdfsd sdfs sdfs dfsdf sdfsdf sdfsdf sdf sdf sdfs dfs  g sdffsd  dgfsdfgfdg sdfsd 234'

            inputSearch.send_keys(mensaje)

            time.sleep(2)

            inputSearch.send_keys(Keys.ENTER)


            # contact_title.send_keys('Hola, éste es un mensajes de prueba que estoy enviando para probar un aplicativo que estoy realizando para la empresa. No tienes que responder a éste mensaje por tanto. Saludos.')
            # contact_title.send_keys(Keys.ENTER)
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
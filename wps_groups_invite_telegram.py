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

CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

class HomePageTests(unittest.TestCase):

    def setUp(self) -> None:
        
        # self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        pathChromeDriver = 'C:/Users/admin/projects/wpsender/chromedriver.exe'
        s = Service(pathChromeDriver)
        
        options = webdriver.ChromeOptions()
        options.add_argument(CHROME_PROFILE_PATH)
        self.driver = webdriver.Chrome(service=s,options=options)
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_getMsgInterface(self):
        driver = self.driver
        driver.implicitly_wait(60)
        # contact_errors = pd.DataFrame(columns=["celular"])

        # contact_names = ['Daniel Lesmes','Humbewrewassfd','Fabio Sarmiento']
        # Obtener el input donde se ingresa el número de contacto para buscar el chat
        searchBox = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'

        inputSearch = self.driver.find_element(By.XPATH,searchBox)

        noEnviados = []

        data = pd.read_excel("Data.xlsx")

        viajes = pd.read_excel("Viajes.xlsx")
        # filepath = 'C:/Users/admin/projects/wpsender/images/SencilloSog.png'
        text_msg = 'Únete a nuestro canal de Télegram a través del siguiente link : https://t.me/cargateclogi'
        # text_msg = 'Entúrnate a traves del siguiente formulario: https://script.google.com/macros/s/AKfycbz8m03ARQZlS8EovuSAbuZs8K9OKRDRZGd6lakGycBsEm5E6q74g718ZY7MkC7HrBFf/exec'
        # text_msg = 'Únete a nuestro grupo de Facebook en donde estaremos compartiendo informacion de cargas disponibles: https://www.facebook.com/groups/1044859782961088/'
        # text_msg = 'Hola, somos Teclogi Cargo, empresa de Transporte de Carga y te invitamos a unirte a nuestro grupo de whatsapp para que estés al tanto de las cargas que tenemos disponibles para ti a través del siguiente link: https://chat.whatsapp.com/LliDLmK55Y1B3kF9iEELow'
        for index, row in data.iterrows():
            contact_name = row['contact_name']

            try:
                # Esperar a que cargue la página, máximo por 15 segundos
                # Asegurarse de que está limpio el input
                wait = WebDriverWait(self.driver,5)
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
                                
                # msg_array = ["Buen día!!!👍",
                #     "Se requiere:",
                #     "*Tipo de vehículo:* Turbo",
                #     "*Tipo de carrocería:* Furgón",
                #     "*Origen:* Cota",
                #     "*Destino:* Funza",
                #     "*Fecha de cargue*: Hoy viernes"
                # ]

                # print(msg_array)
                # for m in msg_array:
                    # print(m)
                    # inputMessage.send_keys(m)
                    # inputMessage.send_keys(Keys.SHIFT,Keys.ENTER)
                    # inputMessage.send_keys(Keys.ENTER)
                # inputMessage.send_keys(Keys.ENTER)

                # file = open('C:/Users/admin/projects/wpsender/cargas/carga.txt','r', encoding="utf8")

                # for line in file:
                #     inputMessage.send_keys(line)
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.ENTER)

                # ->>>>>>>>>>>Invitación grupo de telegram
                inputMessage.send_keys("Buen día!")
                inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                inputMessage.send_keys("Únete a nuestro canal de Télegram a través del siguiente link :")
                inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                inputMessage.send_keys("https://t.me/cargateclogi")
                inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                inputMessage.send_keys("Te esperamos!!!")
                inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                inputMessage.send_keys(Keys.ENTER)
                # ->>>>>>>>>>>Invitación grupo de telegram

                # >>>>>>>>>>>>
                # inputMessage.send_keys("Buen día!")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("Se requiere:")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("Vehículo: Patineta")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("Carrocería: Contenedor HighCube")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("Peso mercancía: 4 ton")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(">>>>: Origen: Tocancipá")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(">>>>: Destino: Barranquilla")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("Observaciones: Estrictamente contenedor HighCube")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("Para mayor información contacta a:")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("https://wa.me/573212573885")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("https://wa.me/573212884773")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys("https://wa.me/573176439755")
                # inputMessage.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                # inputMessage.send_keys(Keys.ENTER)
                # <<<<<<<<<<<<

                time.sleep(1)

            except:
                noEnviados.append([row['contact_name']])

        dfNoenviados = pd.DataFrame(noEnviados)
        dfNoenviados.to_csv('WpsNoEnviados.csv')
        time.sleep(30)
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
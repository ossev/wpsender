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

CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\Teclovers\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

class HomePageTests(unittest.TestCase):

    def setUp(self) -> None:
        
        # self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        pathChromeDriver = 'C:/Users/Teclovers/projects/wpsender/chromedriver.exe'
        s = Service(pathChromeDriver)
        
        options = webdriver.ChromeOptions()
        options.add_argument(CHROME_PROFILE_PATH)
        self.driver = webdriver.Chrome(service=s,options=options)
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        driver.maximize_window()
        time.sleep(10)
        driver.implicitly_wait(30)

    def test_getMsgInterface(self):
        driver = self.driver
        driver.implicitly_wait(30)
        # contact_errors = pd.DataFrame(columns=["celular"])

        # contact_names = ['Daniel Lesmes','Humbewrewassfd','Fabio Sarmiento']
        # Obtener el input donde se ingresa el número de contacto para buscar el chat
        searchBox = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'

        

        # inputSearch = self.driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')

        noEnviados = []
        data = pd.read_excel("Data.xlsx")
        viajes = pd.read_excel("Viajes.xlsx")

        images = [
            '1.png'
        ]


        text_msg = 'Para más información sobre *cargas disponibles* contáctanos por el siguiente link https://wa.me/573156460636. Para *soporte* al conductor contáctanos por el siguiente link https://wa.me/573156460636. Descarga nuestra app android en el siguiente link: https://bit.ly/3khJFXQ y para Huawei con el siguiente link: https://appgallery.huawei.com/app/C104912645'
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


                for img in images:

                    # Image to send
                    filepath = 'C:/Users/Teclovers/projects/wpsender/images/{}'.format(img)

                    # inputMessage_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
                    # inputMessage = wait.until(lambda driver:self.driver.find_element(By.XPATH,inputMessage_xpath))

                    # mensaje = row['message']
                    # inputMessage.send_keys(mensaje)
                    # attachment_box = wait.until(lambda driver:self.driver.find_element(By.XPATH,'//div[@title = "Attach"]'))
                    attachment_box = wait.until(lambda driver:self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'))
                    attachment_box.click()                

                    image_box = wait.until(lambda driver:self.driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
                    image_box.send_keys(filepath)

                    # inputMessage.send_keys(Keys.ENTER)
                    text_box = wait.until(lambda driver:self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'))

                    # ->>>>>>>>>>>Invitación grupo de telegram
                    text_box.send_keys("Para mayor información contacta a:")
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)

                    # # Johana Obando
                    # text_box.send_keys("   3212573885")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys("   https://wa.me/573212573885")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # # Johana Obando

                    # Neftalí Mendez
                    text_box.send_keys("   3184603246")
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys("   https://wa.me/573184603246")
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # Neftalí Mendez

                    # # Adriana Cañón
                    # text_box.send_keys("   3212884773")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys("   https://wa.me/573212884773")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # # Adriana Cañón

                    # # Liseth Díaz
                    # text_box.send_keys("   3176439755")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys("   https://wa.me/573176439755")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # # Liseth Díaz

                    # # Daniel Lesmes
                    # text_box.send_keys("   3058676657")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys("   https://wa.me/573058676657")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # # Daniel Lesmes

                    # # Wilmar Cárdenas
                    # text_box.send_keys("   3184603246")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys("   https://wa.me/573184603246")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # # Wilmar Cárdenas

                    # # Lady Pinzón
                    # text_box.send_keys("   3173670541")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys("   https://wa.me/573173670541")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # # Lady Pinzón

                    # # Andrés Corredor
                    # text_box.send_keys("   3160101982")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys("   https://wa.me/573160101982")
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # # Andrés Corredor

                    text_box.send_keys("   Descarga nuestra app para Android en el siguiente link: https://bit.ly/3khJFXQ")
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys("   Descarga nuestra app para Huawei en el siguiente link: https://appgallery.huawei.com/app/C104912645")
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys("   Conéctate a nuestro grupo de Télegram a través de https://t.me/cargateclogi")
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    text_box.send_keys("Te esperamos")
                    text_box.send_keys(Keys.LEFT_SHIFT,Keys.ENTER)
                    # ->>>>>>>>>>>Invitación grupo de telegram

                    send_button = wait.until(lambda driver:self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span'))
                    send_button.click()
                    time.sleep(1)

            except:
                noEnviados.append([row['contact_name']])

        dfNoenviados = pd.DataFrame(noEnviados)
        dfNoenviados.to_csv('WpsNoEnviados.csv')
        time.sleep(60)
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
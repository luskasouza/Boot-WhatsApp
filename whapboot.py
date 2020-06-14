from selenium import webdriver
import time


class WhatsappBoot:
    def __init__(self):
        self.mensagem = "Olá, Bom dia"
        self.grupos = ["FAMÍLIA"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time, slice(40)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(5)
            grupo.click()
            chatBox = self.driver.find_element_by_class_name('_13ngZ')
            time.sleep(5)
            chatBox.click()
            chatBox.send_keys(self.mensagem)
            buttonEnvia = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(5)
            buttonEnvia.click()
            time.sleep(5)


boot = WhatsappBoot()
boot.EnviarMensagens()

# py.exe whapBoot.py or python whatsapp

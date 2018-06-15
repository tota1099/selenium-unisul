from selenium import webdriver
from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By
import time


class MinhaUnisul(PageObject):
    fieldUser = PageElement(id_='userid')
    fieldPassword = PageElement(id_='pwd')
    buttonAcessar = PageElement(id_='subEnviar')

    def logar(self, usuario, senha):
        self.fieldUser.send_keys(usuario)
        self.fieldPassword.send_keys(senha)
        self.buttonAcessar.click()


chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images': 2, 'disk-cache-size': 4096}
chromeOptions.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chromeOptions)

siteLink = 'https://minha.unisul.br/'

try:
    minhaUnisul = MinhaUnisul(browser, siteLink)
    minhaUnisul.get('psp/pa89prd/?cmd=login&languageCd=POR')
    minhaUnisul.logar('renan.porto', 'yourpassword')
    time.sleep(3)
    minhaUnisul.w.find_element_by_link_text('Notas de Avaliação').click()
    minhaUnisul.w.switch_to.frame(minhaUnisul.w.find_element_by_id('d_conteudo'))
    minhaUnisul.w.find_element_by_link_text('2018 - 1º Semestre').click()
    time.sleep(2)
    table = minhaUnisul.w.find_element_by_class_name('PSLEVEL1GRID')
    rows = table.find_elements(By.TAG_NAME, "tr")

    dados = {}
    for row in rows:
        col = row.find_elements(By.TAG_NAME, "td")
        if col:
            disciplina = col[0].text
            dados[disciplina] = {}

    for disciplina in dados.keys():
        minhaUnisul.w.find_element_by_link_text(disciplina).click()
        table = minhaUnisul.w.find_element_by_class_name('PSLEVEL1GRID')
        rows2 = table.find_elements(By.TAG_NAME, "tr")
        for row2 in rows2:
            col2 = row2.find_elements(By.TAG_NAME, "td")
            if col2:
                atividadeNome = col2[3].text
                atividadeNota = col2[5].text
                dados[disciplina][atividadeNome] = atividadeNota
        minhaUnisul.w.find_element_by_link_text("Selecionar Disciplina/UA").click()
        time.sleep(2)

    print(dados)
except ValueError:
    print(ValueError)
finally:
    browser.quit()

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

	def entrarUltimoSemestre(self):
		table = PageElement(class_name='PSGROUPBOX')

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096 }
chromeOptions.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chromeOptions)

siteLink = 'https://minha.unisul.br/'

try:
	minhaUnisul = MinhaUnisul(browser, siteLink)
	minhaUnisul.get('psp/pa89prd/?cmd=login&languageCd=POR')
	minhaUnisul.logar('renan.porto','yourpassword')
	time.sleep(2)
	minhaUnisul.w.find_element_by_link_text('Notas de Avaliação').click()
	minhaUnisul.w.switch_to.frame(minhaUnisul.w.find_element_by_id('d_conteudo')) 
	minhaUnisul.w.find_element_by_link_text('2018 - 1º Semestre').click()
	time.sleep(2)
	table = minhaUnisul.w.find_element_by_class_name('PSLEVEL1GRID')
	rows = table.find_elements(By.TAG_NAME, "tr")
	for row in rows:  
  		col = row.find_elements(By.TAG_NAME, "td")
  		if col:
  			print(col[0].text)
except ValueError:
	print(ValueError)
finally:
	browser.quit()


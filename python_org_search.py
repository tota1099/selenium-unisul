from selenium import webdriver
from page_objects import PageObject, PageElement

class Google(PageObject):
	search_bar = PageElement(id_='lst-ib')
	btn_search = PageElement(name="btnK")
	btn_lucky = PageElement(name='btnI')

	def search(self, text):
		self.search_bar.send_keys(text)
		self.btn_search.click()

browser = webdriver.Firefox()

google = Google(browser, 'http://google.com/')
google.get('')
google.search('Live de python')
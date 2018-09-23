import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MinhaUnisul.MinhaUnisulEnum import Columns, Buttons


class MinhaUnisul():
    site_url = 'https://minha.unisul.br/'

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(self.site_url + 'psp/pa89prd/?cmd=login&languageCd=POR')

    def login(self):
        user = os.environ['USER_NAME']
        password = os.environ['USER_PASSWORD']
        self.browser.find_element_by_id(Buttons.USER_FIELD_ID.value).send_keys(user)
        self.browser.find_element_by_id(Buttons.PASSWORD_FIELD_ID.value).send_keys(password)
        self.browser.find_element_by_id(Buttons.ACCESS_BUTTON_ID.value).click()

        url = self.browser.current_url
        if url.find('errorCode=105') > 0:
            self.browser.quit()
            raise ValueError('Seu ID Usuário e/ou Senha não é válido.')

    def enter_menu_grades(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Notas de Avaliação"))
            )
            self.browser.find_element_by_link_text('Notas de Avaliação').click()
        except ValueError:
            self.browser.quit()

    def enter_semester(self):
        try:
            semester = os.environ['USER_SEMESTRE']
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.presence_of_element_located((By.ID, 'd_conteudo')))
            self.browser.switch_to.frame(self.browser.find_element_by_id('d_conteudo'))
            self.browser.find_element_by_link_text(semester + "º Semestre").click()
        except ValueError:
            self.browser.quit()

    def get_disciplines(self):

        try:
            table = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "PSLEVEL1GRID"))
            )
        except ValueError:
            self.browser.quit()

        rows = table.find_elements(By.TAG_NAME, "tr")

        disciplines = {}
        for row in rows:
            col = row.find_elements(By.TAG_NAME, "td")
            if col:
                discipline = col[Columns.DISCIPLINE.value].text
                disciplines[discipline] = {}
        return disciplines

    def get_disciplines_grades(self, disciplines):
        disciplines_grades = {}

        for discipline in disciplines.keys():
            if discipline not in disciplines_grades:
                disciplines_grades[discipline] = {}
            self.browser.find_element_by_link_text(discipline).click()
            table = self.browser.find_element_by_class_name('PSLEVEL1GRID')
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if cols:
                    work_name = cols[Columns.WORK_NAME.value].text
                    work_grade = cols[Columns.WORK_GRADE.value].text
                    if work_grade.strip() != '':
                        disciplines_grades[discipline][work_name] = work_grade
            self.browser.find_element_by_link_text("Selecionar Disciplina/UA").click()

        return disciplines_grades

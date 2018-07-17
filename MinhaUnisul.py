import os
from selenium.webdriver.common.by import By
from MinhaUnisulEnum import Columns, Buttons


class MinhaUnisul():
    site_url = 'https://minha.unisul.br/'

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(self.site_url + 'psp/pa89prd/?cmd=login&languageCd=POR')

    def logar(self):
        usuario = os.environ['USER_NAME']
        senha = os.environ['USER_PASSWORD']
        self.browser.find_element_by_id(Buttons.USER_FIELD_ID.value).send_keys(usuario)
        self.browser.find_element_by_id(Buttons.PASSWORD_FIELD_ID.value).send_keys(senha)
        self.browser.find_element_by_id(Buttons.ACCESS_BUTTON_ID.value).click()

    def entrar_notas_avaliacoes(self):
        self.browser.find_element_by_link_text('Notas de Avaliação').click()

    def entrar_semestre(self):
        semestre = os.environ['USER_SEMESTRE']
        self.browser.switch_to.frame(self.browser.find_element_by_id('d_conteudo'))
        self.browser.find_element_by_link_text(semestre + "º Semestre").click()

    def get_disciplines(self):
        table = self.browser.find_element_by_class_name('PSLEVEL1GRID')
        rows = table.find_elements(By.TAG_NAME, "tr")

        disciplines = {}
        for row in rows:
            col = row.find_elements(By.TAG_NAME, "td")
            if col:
                discipline = col[0].text
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
                    work_name = cols[Columns.WORK_NAME_COLUMN.value].text
                    work_grade = cols[Columns.WORK_GRADE_COLUMN.value].text
                    disciplines_grades[discipline][work_name] = work_grade
            self.browser.find_element_by_link_text("Selecionar Disciplina/UA").click()

        return disciplines_grades

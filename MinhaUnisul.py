from selenium.webdriver.common.by import By
from selenium import webdriver

class MinhaUnisul(webdriver):
    site_url = 'https://minha.unisul.br/'

    def __init__(self):
        self.get(self.site_url + 'psp/pa89prd/?cmd=login&languageCd=POR')

    def logar(self, usuario, senha):
        self.w.find_element_by_id('userid').send_keys(usuario)
        self.w.find_element_by_id('pwd').send_keys(senha)
        self.w.find_element_by_id('subEnviar').click()

    def entrar_notas_avaliacoes(self):
        self.w.find_element_by_link_text('Notas de Avaliação').click()

    def entrar_atual_semestre(self):
        self.w.switch_to.frame(self.w.find_element_by_id('d_conteudo'))
        self.w.find_element_by_link_text('2018 - 1º Semestre').click()

    def get_disciplines(self):
        table = self.w.find_element_by_class_name('PSLEVEL1GRID')
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
            self.w.find_element_by_link_text(discipline).click()
            table = self.w.find_element_by_class_name('PSLEVEL1GRID')
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cols = linha.find_elements(By.TAG_NAME, "td")
                if cols:
                    work_name = colunas[3].text
                    work_grade = colunas[5].text
                    disciplines_grades[discipline][work_name] = work_grade
            self.w.find_element_by_link_text("Selecionar Disciplina/UA").click()

        return disciplines_grades

import MinhaUnisul
import BrowserChrome

try:
    browser = BrowserChrome.get()
    minhaUnisul = MinhaUnisul(browser)
    minhaUnisul.logar('renan.porto', '#JOAO.2016!')
    minhaUnisul.entrar_notas_avaliacoes()
    minhaUnisul.entrar_atual_semestre()
    disciplines = minhaUnisul.get_disciplines()
    disciplines_grades = minhaUnisul.get_disciplines_grades(disciplines)
except ValueError:
    print(ValueError)
finally:
    browser.quit()

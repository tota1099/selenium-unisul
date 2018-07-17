import os
from dotenv import load_dotenv
from MinhaUnisul import MinhaUnisul
import BrowserChrome

try:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_folder = os.path.expanduser(dir_path)
    load_dotenv(os.path.join(project_folder, '.env'))
    browser = BrowserChrome.get()
    minhaUnisul = MinhaUnisul(browser)
    minhaUnisul.login()
    minhaUnisul.enter_menu_grades()
    minhaUnisul.enter_semester()
    disciplines = minhaUnisul.get_disciplines()
    disciplines_grades = minhaUnisul.get_disciplines_grades(disciplines)
    browser.quit()
except ValueError:
    print(ValueError)

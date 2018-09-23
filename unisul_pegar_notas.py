import os
from dotenv import load_dotenv
from MinhaUnisul.MinhaUnisul import MinhaUnisul
from services.GradesProcess import GradesProcess
from services.Mail import Mail
from browser import BrowserChrome
import json

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
    gradesProcess = GradesProcess(disciplines_grades)
    disciplines_grades_news = gradesProcess.get_disciplines_grades_news()
    if disciplines_grades_news:
        mail = Mail()
        mail.send(disciplines_grades_news)
    with open('disciplines_grades.json', 'w') as outfile:
        json.dump(disciplines_grades, outfile)
except ValueError as e:
    print(e)
finally:
    browser.quit()

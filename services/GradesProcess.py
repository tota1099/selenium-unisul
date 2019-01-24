import json
import os

class GradesProcess():
    
    def __init__(self, grades):
        self.grades = grades

    def get_disciplines_grades_news(self):
        old_grades = self.get_current_disciplines_grades()
        old_grades = json.loads(old_grades)
        disciplines_grades_news = {}

        for discipline, grades in self.grades.items():

            if discipline not in old_grades:
                old_grades[discipline] = {}

            for work, grade in grades.items():
                if grade.strip() != '' and work not in old_grades[discipline]:
                    if discipline not in disciplines_grades_news:
                        disciplines_grades_news[discipline] = {}
                    disciplines_grades_news[discipline][work] = grade

        return disciplines_grades_news



    def get_current_disciplines_grades(self):
        if os.path.exists('disciplines_grades.json'):
            disciplines_grades  = open('disciplines_grades.json','r')
            return disciplines_grades.read()
        return "{}"

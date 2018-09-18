import json

class GradesProcess():
    
    def __init__(self, grades):
        self.grades = grades

    def get_disciplines_grades_news(self):
        old_grades = self.get_current_disciplines_grades()
        old_grades = json.loads(old_grades)
        disciplines_grades_news = {}

        for discipline, grades in self.grades.items():
            if discipline in old_grades:
                for grade, nota in grades.items():
                    if grade not in old_grades.get(discipline):
                        if discipline not in disciplines_grades_news:
                            disciplines_grades_news[discipline] = {}
                        disciplines_grades_news[discipline][grade] = nota
            else:
                disciplines_grades_news[discipline] = grades
        return disciplines_grades_news



    def get_current_disciplines_grades(self):
        disciplines_grades  = open('disciplines_grades.json','r')
        return disciplines_grades.read()

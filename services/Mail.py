import smtplib
import jinja2
from email.mime.text import MIMEText
from email.message import EmailMessage
import os

class Mail():
    
    def __init__(self):
       pass

    def get_mail_message(self, new_grades):
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template('new_grades.html')
        return template.render(new_grades=new_grades)

    def send(self, new_grades):
        message = EmailMessage()
        message.set_content(MIMEText(self.get_mail_message(new_grades), 'html'))

        message['Subject'] = 'Nova nota no sistema!'
        message['From'] = os.environ['EMAIL_FROM']
        message['To'] = os.environ['EMAIL_TO']

        # Send the message via our own SMTP server.
        server = smtplib.SMTP(os.environ['EMAIL_SERVER'], os.environ['EMAIL_PORT'])
        server.starttls()
        server.login(os.environ['EMAIL_SERVER_USER'], os.environ['EMAIL_SERVER_PASS'])
        server.send_message(message)
        server.quit()
        
if __name__ == "__main__":
    mail = Mail()
    mail.test()
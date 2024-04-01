from bottle import post, request
import re

# Паттерн для проверки адреса электронной почты
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

@post('/home')
def my_form():
    quest = request.forms.get('QUEST')
    name = request.forms.get('NAME')
    mail = request.forms.get('ADRESS')
    date = request.forms.get('DATE')

    if not (quest and name and mail and date):
        return "Please fill in all fields."

    if email_pattern.match(mail):
        return "Thanks %s! The answer will be sent to the email %s Access Date: %s" % (name, mail, date)
    else:
        return "Invalid email address. Please enter a valid email address."

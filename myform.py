from bottle import post, request
import re

# Паттерн для проверки адреса электронной почты
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

@post('/home')
def my_form():
    mail = request.forms.get('ADRESS')
    name = request.forms.get('NAME')

    if email_pattern.match(mail):
        return "Thanks %s! The answer will be sent to the email %s" % (name, mail)
    else:
        return "Invalid email address. Please enter a valid email address."

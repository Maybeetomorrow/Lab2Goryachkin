from bottle import post, request
import re

# Паттерн для проверки адреса электронной почты
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

@post('/home')
def my_form():
    # Получаем данные из формы
    quest = request.forms.get('QUEST')  # Получаем вопрос
    name = request.forms.get('NAME')    # Получаем имя
    mail = request.forms.get('ADRESS')  # Получаем адрес электронной почты
    date = request.forms.get('DATE')    # Получаем дату

    # Проверяем, заполнены ли все поля формы
    if not (quest and name and mail and date):
        return "Please fill in all fields."

    # Проверяем, соответствует ли адрес электронной почты заданному шаблону
    if email_pattern.match(mail):
        # Если адрес электронной почты действителен, возвращаем сообщение об успешной отправке формы
        return "Thanks %s! The answer will be sent to the email %s Access Date: %s" % (name, mail, date)
    else:
        # Если адрес электронной почты недействителен, возвращаем сообщение об ошибке
        return "Invalid email address. Please enter a valid email address."

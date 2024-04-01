from bottle import post, request
import re
from datetime import datetime, date

# Паттерн для проверки адреса электронной почты
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

@post('/home')
def my_form():
    # Получаем данные из формы
    quest = request.forms.get('QUEST')  # Получаем вопрос
    name = request.forms.get('NAME')    # Получаем имя
    mail = request.forms.get('ADRESS')  # Получаем адрес электронной почты
    date_str = request.forms.get('DATE')    # Получаем дату в виде строки

    # Проверяем, заполнены ли все поля формы
    if not (quest and name and mail and date_str):
        return "Please fill in all fields."

    # Проверяем, соответствует ли адрес электронной почты заданному шаблону
    if not email_pattern.match(mail):
        return "Invalid email address. Please enter a valid email address."

    # Проверяем введенную дату
    try:
        # Преобразуем строку даты в объект datetime
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        # Получаем текущую дату
        current_date = date.today()
        # Получаем год из введенной даты
        year = date.year
        # Проверяем, что введенная дата не больше текущей даты
        if date > current_date:
            return "Date cannot be greater than current date."
        # Проверяем, что год не меньше заданного минимального значения
        min_year = 2000
        if year < min_year:
            return "Year cannot be less than %d." % min_year
    except ValueError:
        return "Invalid date format. Please enter date in YYYY-MM-DD format."

    # Если все проверки пройдены успешно, возвращаем сообщение об успешной отправке формы
    return "Thanks %s! The answer will be sent to the email %s Access Date: %s" % (name, mail, date_str)

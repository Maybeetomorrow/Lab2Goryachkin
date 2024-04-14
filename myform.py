from bottle import post, request, abort
import re
import pdb
from datetime import datetime, date

# Паттерн для проверки адреса электронной почты
email_pattern = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,10}$')

# Паттерн для проверки имени
name_pattern = re.compile(r'^[a-zA-Z0-9_]{1,20}$')

@post('/home')
def my_form():
    # Получаем данные из формы
    quest = request.forms.get('QUEST')  # Получаем вопрос
    name = request.forms.get('NAME')    # Получаем имя
    mail = request.forms.get('ADRESS')  # Получаем адрес электронной почты
    date_str = request.forms.get('DATE')    # Получаем дату в виде строки

    #Функция записи данных в словарь
    def process_form(mail,name, text):
        questions = {}        
        # Записываем данные в словарь
        questions[mail] = [name, text]
        
        # Выводим словарь для проверки
        pdb.set_trace()  # Точка останова после вызова функции
        return "Thanks! The answer will be sent to the mail %s" % mail

    # Проверяем, заполнены ли все поля формы
    if not (quest and name and mail and date_str):
        abort(400, "Please fill in all fields.")

    # Проверяем, соответствует ли адрес электронной почты заданному шаблону=
    if not email_pattern.match(mail):
        abort(400, "Invalid email address. Please enter a valid email address.")

    # Проверяем правильность ввода имени
    if not name_pattern.match(name):
        abort(400, "Invalid name format. Please enter a name without spaces and '@' and with a maximum length of 20 characters.")

    # Проверяем максимальную длину вопроса
    if len(quest) > 255:
        abort(400, "Question length is too large. Maximum length is 255 characters.")

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
            abort(400, "Date cannot be greater than current date.")
        # Проверяем, что год не меньше заданного минимального значения
        min_year = 2000
        if year < min_year:
            abort(400, "Year cannot be less than %d." % min_year)
    except ValueError:
        abort(400, "Invalid date format. Please enter date in YYYY-MM-DD format.")

    process_form(mail,name, quest)
    # Если все проверки пройдены успешно, возвращаем сообщение об успешной отправке формы
    return "Thanks %s! The answer will be sent to the email %s Access Date: %s" % (name, mail, date_str)

import calc

def test_add():
    """
    Тестирование функции add из модуля calc.
    
    Проверяет, что calc.add(1, 2) возвращает 3.
    Если результат правильный, выводит "Test add(a, b) is OK".
    Иначе выводит "Test add(a, b) is Fail".
    """
    if calc.add(1, 2) == 3:
        print("Test add(a, b) is OK")
    else:
        print("Test add(a, b) is Fail")
        
def test_sub():
    """
    Тестирование функции sub из модуля calc.
    
    Проверяет, что calc.sub(4, 2) возвращает 2.
    Если результат правильный, выводит "Test sub(a, b) is OK".
    Иначе выводит "Test sub(a, b) is Fail".
    """
    if calc.sub(4, 2) == 2:
        print("Test sub(a, b) is OK")
    else:
        print("Test sub(a, b) is Fail")
 
def test_mul():
    """
    Тестирование функции mul из модуля calc.
    
    Проверяет, что calc.mul(2, 5) возвращает 10.
    Если результат правильный, выводит "Test mul(a, b) is OK".
    Иначе выводит "Test mul(a, b) is Fail".
    """
    if calc.mul(2, 5) == 10:
        print("Test mul(a, b) is OK")
    else:
        print("Test mul(a, b) is Fail")
 
def test_div():
    """
    Тестирование функции div из модуля calc.
    
    Проверяет, что calc.div(8, 4) возвращает 2.
    Если результат правильный, выводит "Test div(a, b) is OK".
    Иначе выводит "Test div(a, b) is Fail".
    
    Примечание:
    Тест не учитывает деление на 0, что должно вызывать ZeroDivisionError.
    """
    if calc.div(8, 4) == 2:
        print("Test div(a, b) is OK")
    else:
        print("Test div(a, b) is Fail")       

# Запуск тестов
test_add()
test_sub()
test_mul()
test_div()

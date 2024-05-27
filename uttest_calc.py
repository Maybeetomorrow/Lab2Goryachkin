import unittest
import calc

class CalcTest(unittest.TestCase):
    """
    Класс для тестирования функций из модуля calc.
    """

    def test_add(self):
        """
        Тестирование функции add из модуля calc.
        Проверяет, что calc.add(1, 2) возвращает 3.
        """
        self.assertEqual(calc.add(1, 2), 3)
        
    def test_sub(self):
        """
        Тестирование функции sub из модуля calc.
        Проверяет, что calc.sub(4, 2) возвращает 2.
        """
        self.assertEqual(calc.sub(4, 2), 2)
        
    def test_mul(self):
        """
        Тестирование функции mul из модуля calc.
        Проверяет, что calc.mul(2, 5) возвращает 10.
        """
        self.assertEqual(calc.mul(2, 5), 10)
        
    def test_div(self):
        """
        Тестирование функции div из модуля calc.
        Проверяет, что calc.div(8, 4) возвращает 2.
        """
        self.assertEqual(calc.div(8, 4), 2)
        
if __name__ == '__main__':
    unittest.main()

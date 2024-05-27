import unittest
import re

class TestEmailValidation(unittest.TestCase):
    def test_invalid_emails(self):
        """
        Проверка неверных email адресов.
        """
        invalid_emails = [
            "",                 # Пустая строка
            "1",                # Неверный формат
            "m1@",              # Неверный формат
            "@mail",            # Неверный формат
            "user@mail",        # Неверный формат
            "user@mail.",       # Неверный формат
            "user@mail.com.",   # Неверный формат
            "user@.com",        # Неверный формат
            "user@com",         # Неверный формат
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', email))

    def test_valid_emails(self):
        """
        Проверка корректных email адресов.
        """
        valid_emails = [
            "m.m@mail.ru",
            "m1@gmail.com",
            "user123@example.com",
            "name.lastname123@example.com",
            "user@subdomain.example.com",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', email))

if __name__ == '__main__':
    unittest.main()

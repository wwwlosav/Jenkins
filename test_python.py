import unittest
from unittest.mock import patch
from randomTS import guess_the_number

class TestGuessTheNumber(unittest.TestCase):
    @patch('bulitins.input',side_effect=['50'])
    def test_guess_correct(self, mock_input):
        with patch('random.randit',return_valuer=50):
            result = guess_the_number()
            self.assertEqual(result,"Поздравляем! Вы угадали число за 1 попытку. ")

    @patch('builtins.input', side_effect=['30', '50'])
    def test_guess_too_low(self, mock_input):
    # Тест на ввод слишком низкого числа
        with patch('random.randint', return_value=50):
            result = guess_the_number()
            self.assertEqual(result, "Поздравляем! Вы угадали число за 2 попытки.")

    @patch('builtins.input', side_effect=['70', '50'])
    def test_guess_too_high(self, mock_input):
    # Тест на ввод слишком высокого числа
        with patch('random.randint', return_value=50):
            result = guess_the_number()
            self.assertEqual(result, "Поздравляем! Вы угадали число за 2 попытки.")

    @patch('builtins.input', side_effect=['abc', '50'])
    def test_invalid_input(self, mock_input):
    # Тест на ввод некорректных данных (буквы вместо чисел)
        with patch('random.randint', return_value=50):
            result = guess_the_number()
            self.assertEqual(result, "Поздравляем! Вы угадали число за 2 попыток.")

if __name__ == '__main__':
    unittest.main()
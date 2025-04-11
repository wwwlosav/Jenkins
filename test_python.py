import unittest
from unittest.mock import patch
from randomTS import guess_the_number

class TestGuessTheNumber(unittest.TestCase):
    @patch('bulitins.input',side_effect=['50','50'])
    def test_guess_correct(self, mock_input):
        with patch('random.randit',return_valuer=50):
            guess_the_number()

    @patch('builtins.input', side_effect=['30', '50'])
    def test_guess_too_low(self, mock_input):
    # Тест на ввод слишком низкого числа
        with patch('random.randint', return_value=50):
            guess_the_number()

    @patch('builtins.input', side_effect=['70', '50'])
    def test_guess_too_high(self, mock_input):
    # Тест на ввод слишком высокого числа
        with patch('random.randint', return_value=50):
            guess_the_number()

   
if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestGuessTheNumber)

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

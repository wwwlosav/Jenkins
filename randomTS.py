import random

def guess_the_number():
    number_to_guess = random.random() * 100 + 1
    number_to_guess = round(number_to_guess)
    
    attempts = 0
    
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100.")
    print("Чтобы выйти из игры, введите 'выход'.")
    
    while True:
        user_guess = input("Введите ваше число: ")
        
        if user_guess.lower() == "выход":
            print("Вы вышли из игры.")
            break
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Пожалуйста, введите целое число или введите 'выход', чтобы выйти из игры.")
            continue
        
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Ваше число меньше загаданного.")
        elif user_guess > number_to_guess:
            print("Ваше число больше загаданного.")
        else:
            print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
            break

    play_again = input("Хотите сыграть еще раз? (д/н): ")
    if play_again.lower() == "д":
        guess_the_number()
    else:
        print("Спасибо за игру!")

def main():
    print("Добро пожаловать в игру!")
    guess_the_number()

if __name__ == "__main__":
    main()


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

   
if __name__ == '__main__':
    unittest.main()

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



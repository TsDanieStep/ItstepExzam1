import random


def get_user_choice():
    while True:
        choice = input("Выберите камень, ножницы или бумагу: ")
        if choice.lower() in ['камень', 'ножницы', 'бумага']:
            return choice.lower()
        else:
            print("Неверный выбор. Попробуйте еще раз.")


def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif user_choice == 'камень' and computer_choice == 'ножницы':
        return "Вы победили!"
    elif user_choice == 'ножницы' and computer_choice == 'бумага':
        return "Вы победили!"
    elif user_choice == 'бумага' and computer_choice == 'камень':
        return "Вы победили!"
    else:
        return "Вы проиграли."


def play_again():
    while True:
        choice = input("Хотите сыграть еще раз? (да/нет): ")
        if choice.lower() == 'да':
            return True
        elif choice.lower() == 'нет':
            return False
        else:
            print("Неверный выбор. Попробуйте еще раз.")


def main():
    print("Добро пожаловать в игру камень, ножницы, бумага!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Вы выбрали {user_choice}, компьютер выбрал {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))
        if not play_again():
            break
    print("Спасибо за игру!")



if __name__ == '__main__':
    main()





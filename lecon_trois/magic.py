"""
    Магическое число.
    При запуске программы генерируется число, которое нужно угадать.
    Подсказки: больше или меньше.
    Программа в бесконечном цикле.
    После отгадывания появляется результат: само число, количество попыток,
        а так же вопрос: "Continue? (y/n)"
    * Для генерации случайного числа можно воспользоваться
        функцией random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
"""
import random

while True:
    random_number = random.randint(1, 100)  # случайное число от 1 до 100
    # print(random_number)
    q = 1
    try:
        user_number = int(
            input(
                "Компьютер загадал магическое число. Отгадайте его.\nВаш ответ: "
            )
        )
    except ValueError:
        print("Ошибка ввода! Введите корректно целое число!")
    else:
        while user_number != random_number:
            print("Вы не угадали! Пробуйте дальше))\n")
            q += 1
            if user_number > random_number:
                try:
                    user_number = int(
                        input(
                            "Ваш число больше чем магическое.\nВаш новый ответ: "
                        )
                    )
                except ValueError:
                    print(
                        "Ошибка ввода! Введите корректно целое число!\nВы впустую использовали попытку(\n"
                    )
            elif user_number < random_number:
                try:
                    user_number = int(
                        input(
                            "Ваш число меньше чем магическое.\nВаш новый ответ: "
                        )
                    )
                except ValueError:
                    print(
                        "Ошибка ввода! Введите корректно целое число!\nВы впустую использовали попытку(\n"
                    )
        if user_number == random_number:
            print(
                "\nВы угадали магическое число: ",
                random_number,
                "\nВам потребовалось",
                q,
                "попыток.\n",
            )
            more_play = input("Продолжим играть?\nВведите да/нет")
            while more_play != "да" and more_play != "нет":
                more_play = input("Продолжим играть?\nВведите да/нет")
            if more_play == "нет":
                input("Нажмите любую клавишу для выхода")
                break

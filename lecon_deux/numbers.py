# Программа вычисляет сумму цифр трехзначного числа, вводимого пользователем
# Есть защита от дурака)
# Проводится анализ цифр на возрастающий/убывающий/одинаковый/случайный ряд

try:
    user_number = int(input('Введите число от 1 до 999: '))

    if user_number < 1 or user_number > 999:
        print('Вы ввели число вне рабочего диапазона! Перезапустите программу для корректной работы.')

    else:
        user_number_cents = user_number // 100
        user_number_dix = (user_number - (user_number_cents * 100)) // 10
        user_number_un = user_number - (user_number_cents * 100 + user_number_dix * 10)
        sum_of_numbers = user_number_cents + user_number_dix + user_number_un
        print('Сумма цифр числа', user_number, 'равна', sum_of_numbers)

        if user_number_cents < user_number_dix < user_number_un:
            print('Возрастание цифр')
        elif user_number_cents > user_number_dix > user_number_un or user_number_cents == 0 and user_number_un == 0 \
                and user_number_dix > 0:
            print('Убывание цифр')
        elif user_number_cents == user_number_dix == 0:
            print('Число однозначное. Убывания/возрастания цифр нет!')
        elif user_number_cents == user_number_dix or user_number_cents == user_number_un or user_number_dix == \
                user_number_un:
            print('Есть одинаковые цифры')
        elif user_number_cents == 0:
            if user_number_dix > user_number_un:
                print('Убывание цифр')
        else:
            print('Цифры вразброс')

except ValueError:
    print('Вы не ввели целое число!\nПопробуйте позже и правильно:)')

# Генератор паролей.

import re
from random import choice, randint
from string import digits, punctuation, ascii_letters


def main():
    print('S.P.Q.R.')

    var_1 = '1'
    var_2 = '2'
    var_3 = '3'
    user_select = input(f'Выберите опцию генерации пароля:\n{var_1} - '
                        f'Сгенерировать простой пароль\n{var_2} - '
                        f'Сгенерировать средний пароль \n'
                        f'{var_3} - Сгенерировать сложный пароль\nВаш выбор: ')
    if user_select not in (var_1, var_2, var_3):
        return main()

    symbols_data_base = digits + punctuation + ascii_letters

    if user_select == var_1:
        user_password = password_wake(symbols_data_base)

    elif user_select == var_2:
        user_password = password_medium(symbols_data_base)

    else:
        user_password = password_power(symbols_data_base)

    print(f'Сгенерированный пароль: {user_password}')


def password_wake(s_d_b):
    password = ''
    for element in range(8):
        element = choice(re.findall(r'[a-z]', s_d_b))
        password += element
    return password


def password_medium(s_d_b):
    password = ''
    for element in range(8):
        element = choice(re.findall(r'[a-zA-Z0-9]', s_d_b))
        password += element
    return password


def password_power(s_d_b):
    password = ''
    for element in range(randint(8, 16)):
        element = choice(s_d_b)
        password += element

    counter_up = counter_lo = counter_di = counter_pu = 0
    for symbol in password:
        if symbol.isdigit():
            counter_di += 1
        elif symbol.islower():
            counter_lo += 1
        elif symbol.isupper():
            counter_up += 1
        else:
            counter_pu += 1
    if counter_di == 0 or counter_pu == 0 or counter_up == 0 or \
            counter_lo == 0:
        print(f'пароль не сложный и будет перегенерирован: {password}')
        return password_power(s_d_b)

    return password


if __name__ == '__main__':
    main()

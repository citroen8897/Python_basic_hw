# Регистрационная форма

import re


def main():
    print('S.P.Q.R\nВас приветствует программа регистрации пользователей\n'
          'Заполните пожалуйста форму регистрации\n')
    travail_un = telephone()
    travail_deux = email()
    travail_trois = password()
    print(f'\nПоздравляем с успешной регистрацией!\n'
          f'Ваш номер телефона: {travail_un}\n'
          f'Ваш e-mail: {travail_deux}\n'
          f'Ваш пароль: {travail_trois}')


def telephone():
    base_op = ('050', '066', '095', '099', '067', '097', '096', '098', '063',
               '073', '093', '044', '045', '068')

    telephone_de_user = input('Введите номер телефона: ')

    for element in telephone_de_user:
        if not element.isdigit():
            telephone_de_user = telephone_de_user.replace(element, '')

    if len(telephone_de_user) < 10 or telephone_de_user[-10:-7] not in base_op:
        print('Неверно введенный номер!\nПопробуйте снова.\n')
        return telephone()
    elif not telephone_de_user.startswith('+38'):
        telephone_de_user = '+38' + telephone_de_user[-10:]
    return telephone_de_user


def email():
    email_de_user = input('Введите e-mail: ')

    if not re.search(r'\w+\.*\w+@\w+\.\w+', email_de_user):
        print('Неверно введенный e-mail! Повторите ввод.\n')
        return email()
    return email_de_user


def password():
    print('***\nТребования к паролю:\nПароль должен содержать:\nБольшую букву'
          '\nмаленькую букву\nцифру\nспецсимвол\nне содержать пробелов'
          '\nдлина пароля минимум 8 символов\n***\n')
    password_de_user = input('Задайте пароль: ')

    if len(password_de_user) < 8 or re.search(r'\s', password_de_user):
        print('0 - Пароль ненадежный. Введите другой.\n')
        return password()
    elif not re.search(r'\d', password_de_user) or \
            not re.search(r'[a-z]', password_de_user) or \
            not re.search(r'[A-Z]', password_de_user) or \
            not re.search(r'[^a-zA-Z0-9]', password_de_user):
        print('1 - Пароль ненадежный. Введите другой.\n')
        return password()

    password_de_user_repond = input('Повторите пароль: ')

    if password_de_user_repond != password_de_user:
        return password()
    return password_de_user


if __name__ == '__main__':
    main()

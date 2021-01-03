# Регистрационная форма

import re


def main():
    print('S.P.Q.R\nВас приветствует программа регистрации пользователей\n'
          'Заполните пожалуйста форму регистрации\n')
    user_phone = get_telephone()
    user_e_post = get_email()
    user_password = get_password()
    print(f'\nПоздравляем с успешной регистрацией!\n'
          f'Ваш номер телефона: {user_phone}\n'
          f'Ваш e-mail: {user_e_post}\n'
          f'Ваш пароль: {user_password}')


def get_telephone():
    base_op = ('050', '066', '095', '099', '067', '097', '096', '098', '063',
               '073', '093', '044', '045', '068')

    phone_user_input = input('Введите номер телефона: ')

    for element in phone_user_input:
        if not element.isdigit():
            phone_user_input = phone_user_input.replace(element, '')

    if len(phone_user_input) < 10 or phone_user_input[-10:-7] not in base_op:
        print('Неверно введенный номер!\nПопробуйте снова.\n')
        return get_telephone()
    elif not phone_user_input.startswith('+38'):
        phone_user_input = '+38' + phone_user_input[-10:]
    return phone_user_input


def get_email():
    email_user_input = input('Введите e-mail: ')

    if not re.search(r'\w+\.*\w+@\w+\.\w+', email_user_input):
        print('Неверно введенный e-mail! Повторите ввод.\n')
        return get_email()
    return email_user_input


def get_password():
    print('***\nТребования к паролю:\nПароль должен содержать:\nБольшую букву'
          '\nмаленькую букву\nцифру\nспецсимвол\nне содержать пробелов'
          '\nдлина пароля минимум 8 символов\n***\n')
    password_user_input = input('Задайте пароль: ')

    if len(password_user_input) < 8 or re.search(r'\s', password_user_input):
        print('0 - Пароль ненадежный. Введите другой.\n')
        return get_password()
    elif not re.search(r'\d', password_user_input) or \
            not re.search(r'[a-z]', password_user_input) or \
            not re.search(r'[A-Z]', password_user_input) or \
            not re.search(r'[^a-zA-Z0-9]', password_user_input):
        print('1 - Пароль ненадежный. Введите другой.\n')
        return get_password()

    password_user_input_confirm = input('Повторите пароль: ')

    if password_user_input_confirm != password_user_input:
        return get_password()
    return password_user_input


if __name__ == '__main__':
    main()

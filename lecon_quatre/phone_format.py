"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.
    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""
print('S.P.Q.R.\n')

while True:
    user_select = input('Ввести телефон или покинуть программу\n'
                        'Ввести телефон - введите 1\n'
                        'Покинуть программу - введите 2\nВаш выбор: ')
    while user_select != '1' and user_select != '2':
        user_select = input('Ввести телефон или покинуть программу\n'
                            'Ввести телефон - введите 1\n'
                            'Покинуть программу - введите 2\nВаш выбор: ')

    if user_select == '1':
        user_telephone = input('Введите телефон: ')

        for a in user_telephone:
            if not a.isdigit():
                user_telephone = user_telephone.replace(a, '')

        if len(user_telephone) < 10 or user_telephone[-10:-7] not in \
                ('050', '066', '095', '099', '067',
                 '097', '096', '098', '063', '093',
                 '073', '044'):
            print('Неверно введенный номер!\nПопробуйте снова или закройте '
                  'программу\n')
        print(user_telephone)

    else:
        break

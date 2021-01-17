import random
import json


def main():
    get_user_name = input('Введи имя: ')
    user_info = {'name': get_user_name.title(),
                 'games': 0,
                 'avg_attempts': 0,
                 'record': 0}
    try:
        file_data_base = open('user_d_b.json', 'r')
    except FileNotFoundError:
        file_data_base = open('user_d_b.json', 'w')
        list_de_users = [user_info]
    else:
        list_de_users = json.load(file_data_base)
        for element in list_de_users:
            if element['name'] == get_user_name.title():
                user_info = element
        list_temp = []
        for element in list_de_users:
            for k, v in element.items():
                if k == 'name':
                    list_temp.append(v)
        if user_info['name'] not in list_temp:
            list_de_users.append(user_info)
    finally:
        file_data_base.close()

    random_number = random.randint(1, 5)
    # print(random_number)
    q = 1
    try:
        user_number = int(input('Компьютер загадал магическое число. '
                                'Отгадайте его.\nВаш ответ: '))
    except ValueError:
        print('Ошибка ввода! Введите корректно целое число!')
    else:
        while user_number != random_number:
            print('Вы не угадали! Пробуйте дальше))\n')
            q += 1
            if user_number > random_number:
                try:
                    user_number = int(input('Ваш число больше чем магическое.'
                                            '\nВаш новый ответ: '))
                except ValueError:
                    print('Ошибка ввода! Введите корректно целое число!\nВы '
                          'впустую использовали попытку(\n')
            elif user_number < random_number:
                try:
                    user_number = int(input('Ваш число меньше чем магическое.'
                                            '\nВаш новый ответ: '))
                except ValueError:
                    print('Ошибка ввода! Введите корректно целое число!\n'
                          'Вы впустую использовали попытку(\n')
        if user_number == random_number:
            print('\nВы угадали магическое число: ', random_number,
                  '\nВам потребовалось', q, 'попыток.\n')

            user_info['games'] += 1

            if q < user_info['record'] or user_info['record'] == 0:
                user_info['record'] = q

            user_info['avg_attempts'] = \
                (user_info['avg_attempts'] * (user_info['games'] - 1) + q) \
                / user_info['games']

            file_data_base = open('user_d_b.json', 'w')
            data_pour_ecrire = json.dumps(list_de_users, indent=4)
            file_data_base.write(data_pour_ecrire)
            file_data_base.close()

            more_play = input('Продолжим играть?\nВведите да/нет')
            if more_play == 'да':
                return main()
            if more_play != 'да':
                input('Нажмите любую клавишу для выхода')
                exit()


if __name__ == '__main__':
    main()

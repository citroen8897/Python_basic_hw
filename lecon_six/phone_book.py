"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).
    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""
import re


def main():
    data_base_1 = []
    with open('phone_book.txt') as file:
        for line in file.readlines():
            line.strip()
            data_base_1.append(line)

    data_base_2 = []
    for element in data_base_1:
        if re.search(r'M|m\S+', element) or re.search(r'\S+A|a\s', element):
            data_base_2.append(element)

    user_numero = 0
    for element in data_base_2:
        user_name = ''
        user_telephone = ''
        for a in element:
            if a.isdigit():
                user_telephone += a
            elif a.isalpha():
                user_name += a
        user_telephone = '+380' + user_telephone[-9:]
        user_numero += 1
        user_info = f'{str(user_numero)}. {user_telephone} - {user_name}\n'
        with open('edited_phone_book.txt', 'a') as file:
            file.write(user_info)


if __name__ == '__main__':
    main()

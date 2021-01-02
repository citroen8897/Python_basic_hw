"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""


def main():
    with open('file_practice.txt', 'w') as file:
        file.write('Starting practice with files\n')


if __name__ == '__main__':
    main()

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""


def main():
    with open('file_practice.txt') as file:
        string_1 = file.read(5)
        string_1 = string_1.upper()
        file.seek(0)
        string_2 = file.read()
        print('Первые 5 символов: ', string_1)
        print('Файл целиком: ', string_2)


if __name__ == '__main__':
    main()

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""


def main():
    with open('text.txt', 'w') as file:
        string_3 = 'Proin laoreet dui vel libero dapibus vehicula vitae ' \
                   'eget turpis.\nNam non eros eu elit posuere posuere id ' \
                   'ac turpis.\nQuisque nec orci blandit, lobortis felis ' \
                   'non, eleifend felis.\nVivamus at odio at lacus viverra ' \
                   'luctus et ut mauris.\nEtiam vehicula nibh eu quam ' \
                   'feugiat tempus.'
        file.write(string_3)
    with open('text.txt') as file:
        string_4 = file.read()
    if string_4.count('i') > string_4.count('e'):
        string_4 = string_4.replace('e', 'i')
    else:
        string_4 = string_4.replace('i', 'e')
    with open('file_practice.txt', 'a') as file:
        file.write(string_4)


if __name__ == '__main__':
    main()

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""


def main():
    with open('file_practice.txt') as file:
        string_5 = file.read()
    with open('file_practice.txt', 'w') as file:
        temp_1 = string_5.count(' ') + string_5.count('\n')
        if (len(string_5) - temp_1) % 2 == 0:
            string_5 = string_5 + '\nthe end'
        else:
            string_5 = string_5 + '\nbye'
        file.write(string_5)
    with open('file_practice.txt') as file:
        print(file.read())


if __name__ == '__main__':
    main()

"""
    5.*
    В средину файла file_practice.txt вставить строку '*some inserted text*'
"""

# решение "по символам"


# def main():
#     s_1 = '*some inserted text*'
#     with open('file_practice.txt') as file:
#         s_2 = file.read()
#     temp_2 = len(s_2) // 2
#     s_2 = s_2[:temp_2] + s_1 + s_2[temp_2:]
#     with open('file_practice.txt', 'w') as file:
#         file.write(s_2)
#
#
# if __name__ == '__main__':
#     main()


# решение по строкам


def main():
    s_1 = ['*some inserted text*']
    s_1_1 = ['*some inserted text*\n']
    with open('file_practice.txt') as file:
        s_2 = file.readlines()
    if len(s_2) % 2 == 0:
        temp_1 = len(s_2) // 2
        s_2 = s_2[:temp_1] + s_1_1 + s_2[temp_1:]
    else:
        temp_1 = len(s_2) // 2
        temp_2 = len(s_2[temp_1]) // 2
        s_2[temp_1] = s_2[temp_1][:temp_2] + s_1[0] + s_2[temp_1][temp_2:]
    with open('file_practice.txt', 'w') as file:
        file.writelines(s_2)


if __name__ == '__main__':
    main()

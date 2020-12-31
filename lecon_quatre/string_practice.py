# Упражнение 1
# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
print('S.P.Q.R.\n')

string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'
string_modify = string.replace(', ', ' ')
print(f'Исходная строка: {string}\nОбработанная строка: {string_modify}')

# Упражнение 2
# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53
print(f'Индекс последней буквы "s" равен: {string_modify.rfind("s")}')

# Упражнение 3
# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6
print(string_modify.count('i') + string_modify.count('I'))

# Упражнение 4
# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)
index_start = string_modify.find('simply dummy text')
index_end = index_start + len('simply dummy text')
print(string_modify[index_start:index_end])

# Упражнение 5
# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy
#    tLorem Ipsum is simply dummy text of the printing industry.'

string_modify_un = string_modify[:(len(string_modify) // 2)] * 3
string_modify_deux = string_modify[(len(string_modify) // 2):]
print(f'Новая строка: {string_modify_un}' + f'{string_modify_deux}')

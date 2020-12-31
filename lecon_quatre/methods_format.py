# Упражнение 1
# 1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
# если больше в верхнем - вывести все в верхнем,
# если поровну - вывести в противоположных регистрах.

# можно заменить данную строку на input()
print('S.P.Q.R.\n')

string_user = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, ' \
              'INDUSTRY.DDDDDDDD'

q_upper = 0
q_lower = 0

for a in range(len(string_user)):
    if string_user[a].isupper():
        q_upper += 1
    elif string_user[a].islower():
        q_lower += 1

print(f'В верхнем регистре символов: {q_upper}\nв нижнем регистре символов: '
      f'{q_lower}')

if q_upper > q_lower:
    string_user_modify = string_user.upper()
    print(f'Исходная строка: {string_user}\nОбработанная строка: '
          f'{string_user_modify}')
elif q_lower > q_upper:
    string_user_modify = string_user.lower()
    print(f'Исходная строка: {string_user}\nОбработанная строка: '
          f'{string_user_modify}')
else:
    string_user_modify = string_user.swapcase()
    print(f'Исходная строка: {string_user}\nОбработанная строка: '
          f'{string_user_modify}')


# Упражнение 2
# 2. Если в строке каждое слово начинается с заглавной буквы, тогда
#         добавить в начало строки 'done. '.
#         Иначе заменить первые 5 элементов строки на 'draft: '.
#     (можно использовать метод replace и/или конкатенацию строк + срезы)

# string_user = 'Lorem, Ipsum, Is, Simply, Summy, Text, Of, The, Printing,
# Industry.'
string_user = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, ' \
              'INDUSTRY.DDDDDDDD'

if string_user.istitle():
    string_user_modify = 'done. ' + string_user
else:
    string_user_modify = string_user.replace(string_user[:6], 'draft: ')
print(f'Исходная строка: {string_user}\nОбработанная строка: '
      f'{string_user_modify}')


# Упражнение 3
# 3. Если длина строки больше 20, то обрезать лишние символы до 20.
#     Иначе дополнить строку символами '@' до длины 20.
# (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

string_user = input('Введите строку: ')

if len(string_user) > 20:
    string_user_modify = string_user[:20]
elif len(string_user) < 20:
    string_user_modify = string_user.ljust(20, '&')
else:
    string_user_modify = string_user[:]
print(f'Исходная строка: {string_user}\nОбработанная строка: '
      f'{string_user_modify}')

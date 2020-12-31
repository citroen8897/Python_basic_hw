"""
 Вводится строка.
 1. Вывести количество слов в введенной строке.
 2. Вывести самое длинное слово и его длину.
"""
# В программе реализован алгоритм защиты от случайного ввода нескольких
# пробелов
print('S.P.Q.R.\n')

user_string = input('Введите строку: ')
while len(user_string) == 0:
    user_string = input('Строка не может быть пустой!\nВведите строку: ')

for a in user_string:
    if not a.isdigit() and not a.isalpha() and a != ' ':
        user_string = user_string.replace(a, ' ')

while '  ' in user_string:
    user_string = user_string.replace('  ', ' ')
user_string = user_string.strip()


print('Введенная строка после обработки на лишние и недостающие пробелы:',
      user_string)
q_string_words = int(user_string.count(' ')) + 1
print('Число слов в указанной строке:', q_string_words)

# Вариант через списки
print('Работа через списки. Обрабатывает все одинаковые слова')

L = user_string.split(' ')
L_longest_words = []

for a in L:
    if len(L_longest_words) == 0:
        L_longest_words.append(a)
    elif len(a) > len(L_longest_words[0]) and len(L_longest_words) == 1:
        L_longest_words[0] = a
    elif len(a) == len(L_longest_words[0]):
        L_longest_words.append(a)
    elif len(a) > len(L_longest_words[0]) and len(L_longest_words) > 1:
        L_longest_words = []
        L_longest_words.append(a)

for word in L_longest_words:
    print(f'\nСамое длинное слово в строке: {word}\nДлина слова {word} равна: '
          f'{len(L_longest_words[0])}')


# вариант без списков.
print('\n\nРабота через строки. Отображает только первое самое длинное слово(')
current_word = ''
longest_word = ''
user_string += ' '

for a in user_string:
    if a != ' ':
        current_word += a
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ''
print(f'Самое длинное слово: {longest_word}\nЕго длина: {len(longest_word)} '
      f'символов.')

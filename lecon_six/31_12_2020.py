# Есть файл, в котором содержаться слова разделённые пробелом.
# Например: "abba com mother bill mother com abba dog abba mother com".
# Нужно найти и вывести тройку слов, которые чаще всего встречаются вместе
# (порядок не имеет значения). То есть в моём примере тройки слов это
# "abba com mother", "com mother bill", "mother bill mother" и т.д.
# Тут правильным ответом должно быть "abba com mother" (частота — 3 раза).

s = input('Задайте строку: ')
L = s.split()
L_1 = []
for a in range(len(L) - 2):
    L_1.append([L[a], L[a + 1], L[a + 2]])
for element in L_1:
    element.sort()
L_1.sort()
print(L_1)
while L_1[0] != L_1[-1]:
    for a in L_1:
        if L_1.count(a) < L_1.count(L_1[-1]):
            L_1.pop(L_1.index(a))
        elif L_1.count(a) > L_1.count(L_1[-1]):
            L_1.pop(-1)
print('Количество повторяющихся троек:', len(L_1))
print('Повторяющаяся тройка:', ' '.join(L_1[0]))

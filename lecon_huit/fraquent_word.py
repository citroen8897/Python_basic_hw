"""
    Напишите функцию, которая принимает текст и
    возвращает слово, которое в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    * Если таких слов несколько - приоритет у первого,
        если расположить список в алфавитном порядке.
"""


def frequent_word(text):
    text = text.lower().replace('.', '').split(' ')
    d_1 = {}
    for element in text:
        if element in d_1:
            d_1[element] += 1
        else:
            d_1[element] = 1
    list_temp = []
    for k, v in d_1.items():
        list_temp.append([v, k])
    list_temp.sort()
    if len(list_temp) > 1:
        while list_temp[-1][0] != list_temp[0][0]:
            list_temp.pop(0)
        for element in list_temp:
            element[0], element[1] = element[1], element[0]
    else:
        list_temp[0][0], list_temp[0][1] = list_temp[0][1], list_temp[0][0]
    list_temp.sort()
    return list_temp[0][0]


text = 'Как видно из примера, присвоение по новому ключу расширяет ' \
       'словарь, присвоение по существующему ключу перезаписывает его, а ' \
       'попытка извлечения несуществующего ключа порождает исключение. Для ' \
       'избежания исключения есть специальный метод (см. ниже), или можно ' \
       'перехватывать исключение.'
assert frequent_word(text) == 'исключение'

text = 'a'
assert frequent_word(text) == 'a'

text = 'bb aa cc bb aa cc bb aa cc'
assert frequent_word(text) == 'aa'

text = 'bb Aa Cc bb aA cc BB aa cC'
assert frequent_word(text) == 'aa'

text = 'q w e r t w w e w w q'
assert frequent_word(text) == 'w'

print('All tests passed successfully!')

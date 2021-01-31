"""
    Напишите функцию, которая принимает текст и
    возвращает слово, которое в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    * Если таких слов несколько - приоритет у первого,
        если расположить список в алфавитном порядке.
"""


def frequent_word(text):
    import re

    temp = re.findall(r"\w+", text)
    temp = [i.lower() for i in temp]
    temp = sorted(list(set([(temp.count(i), i) for i in temp])))
    temp = [temp[j] for j in range(len(temp)) if temp[j][0] == temp[-1][0]]
    temp = sorted([(i[1], i[0]) for i in temp])
    return temp[0][0]


text = (
    "Как видно из примера, присвоение по новому ключу расширяет "
    "словарь, присвоение по существующему ключу перезаписывает его, а "
    "попытка извлечения несуществующего ключа порождает исключение. Для "
    "избежания исключения есть специальный метод (см. ниже), или можно "
    "перехватывать исключение."
)
assert frequent_word(text) == "исключение"

text = "a"
assert frequent_word(text) == "a"

text = "bb aa cc bb aa cc bb aa cc"
assert frequent_word(text) == "aa"

text = "bb Aa Cc bb aA cc BB aa cC"
assert frequent_word(text) == "aa"

text = "q w e r t w w e w w q"
assert frequent_word(text) == "w"

print("All tests passed successfully!")

"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, которые не меньше размера его ноги.
    Напишите программу, которая принимает список доступных размеров коньков и
    список размеров ног желающих.
    И выводит наибольшее количество людей,
    которые смогут покататься одновременно.
    Например:
    [in]
    [39, 38, 41, 37] (доступные размеры)
    [40, 39, 41] (размеры ног желающих)
    [out]
    2
    Напишите несколько тестов
"""


def skates(available_sizes, foot_sizes):
    temp_1 = set(available_sizes)
    temp_2 = set(foot_sizes)
    temp_3 = set()
    for i in temp_2:
        try:
            for j in temp_1:
                if i <= j:
                    temp_3.add(i)
                    temp_1.remove(j)
        except RuntimeError:
            continue
    return len(temp_3)


list_1 = [39, 38, 41, 37]
list_2 = [40, 39, 41]
assert skates(list_1, list_2) == 2

list_1 = [39, 38, 41, 37]
list_2 = [36, 37, 38, 40]
assert skates(list_1, list_2) == 4

list_1 = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
list_2 = [44]
assert skates(list_1, list_2) == 1

list_1 = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
list_2 = [46]
assert skates(list_1, list_2) == 0

print('All tests passed successfully')

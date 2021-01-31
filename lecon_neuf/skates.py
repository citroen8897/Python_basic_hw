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
from slow_decorator import time_decorator


@time_decorator
def skates(available_sizes, foot_sizes):
    res_list = []
    for i in available_sizes:
        for j in foot_sizes:
            if j <= i and len(res_list) < len(available_sizes):
                res_list.append(i)
                foot_sizes.remove(j)
    return len(res_list)


list_available = [37, 38, 39, 40]
list_foot = [37, 37, 40, 40]
assert skates(list_available, list_foot) == 3

list_available = [39, 38, 41, 37]
list_foot = [40, 36, 37, 39]
assert skates(list_available, list_foot) == 4

list_available = [39, 38, 41, 37]
list_foot = [44, 36, 37, 39]
assert skates(list_available, list_foot) == 3

list_available = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
list_foot = [44]
assert skates(list_available, list_foot) == 1

list_available = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
list_foot = [46, 47, 47, 50]
assert skates(list_available, list_foot) == 0

list_available = [39, 39, 39, 39]
list_foot = [37, 37, 40, 39, 39, 39, 39, 40, 40]
assert skates(list_available, list_foot) == 4

print("All tests passed successfully")

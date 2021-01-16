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
    # temp_1 = set(available_sizes)
    # temp_2 = set(foot_sizes)
    # temp_3 = set()
    # for i in temp_2:
    #     try:
    #         for j in temp_1:
    #             if i <= j:
    #                 temp_3.add(i)
    #                 temp_1.remove(j)
    #     except RuntimeError:
    #         continue
    # return len(temp_3)

    res_set = set()
    available_sizes.sort()
    foot_sizes.sort()
    print(available_sizes)
    print(foot_sizes)
    for i in available_sizes:
        for j in foot_sizes:
            if i <= j:
                res_set.add(i)
                foot_sizes.remove(i)
    print(res_set)
    print(available_sizes)
    return len(res_set)


list_available = [39, 38, 41, 37]
list_foot = [40, 39, 41]
assert skates(list_available, list_foot) == 2

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
list_foot = [46]
assert skates(list_available, list_foot) == 0

print('All tests passed successfully')

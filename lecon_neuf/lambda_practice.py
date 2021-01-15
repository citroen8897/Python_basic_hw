data = [
    (2, 'green'), (1, 'blue'), (2, 'yellow'), (1, 'aquamarine'),
    (4, 'red'), (3, 'gold'), (5, 'black'), (2, 'brown'),
    (5, 'pink'), (1, 'purple'), (4, 'white'), (1, 'gray'),
]

# 1. Вывести список data, отсортированный по цвету (2 элемент кортежа).


def func_1(list_input):
    return sorted(list_input, key=lambda element: element[1])


print(func_1(data))
# 2. Отсортировать список по 1 элементу кортежа, а если значения одинаковые,
#    то их отсортировать по 2 элементу. Результат вывести на экран.


def func_2(list_input):
    return sorted(list_input, key=lambda element: (element[0], element[1]))


print(func_2(data))
# 3. С помощью filter() и lambda вывести только те кортежи из списка,
#    цвет которых состоит из 4 букв.


def func_3(list_input):
    return list(filter(lambda element: len(element[1]) == 4, list_input))


print(func_3(data))


# 4. Вывести цвет, которой состоит из найбольшего количества букв.


def func_4(list_input):
    return max(list_input, key=lambda element: len(element[1]))


print(func_4(data))

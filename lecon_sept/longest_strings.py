def longest_strings(list_in):
    # Вариант 1 (10 строк)
    # list_out = list_in[0:1]
    # for element in list_in[1:]:
    #     if len(list_in) == 1:
    #         list_out = list_in[:]
    #     elif len(list_out[0]) == len(element):
    #         list_out.append(element)
    #     elif len(list_out[0]) < len(element):
    #         list_out.clear()
    #         list_out.append(element)
    # return list_out

    # Вариант 2 (6 строк)
    temp_1 = [len(i) for i in list_in]
    while max(temp_1) != min(temp_1):
        list_in.pop(temp_1.index(min(temp_1)))
        temp_1.pop(temp_1.index(min(temp_1)))
    list_out = list_in[:]
    return list_out

    # Вариант 3 (3 строки)
    # list_in.sort(key=len)
    # list_out = [i for i in list_in if len(i) == len(list_in[-1])]
    # return list_out


t_1 = ["x"]
assert longest_strings(t_1) == ["x"]

t_2 = ["abc", "eeee", "abcd", "dcd"]
assert longest_strings(t_2) == ["eeee", "abcd"]

t_3 = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
assert longest_strings(t_3) == ["zzzzzz", "abcdef", "aaaaaa"]

t_4 = ["enyky", "benyky", "yely", "varennyky"]
assert longest_strings(t_4) == ["varennyky"]

t_5 = ["abacaba", "abacab", "abac", "xxxxxx"]
assert longest_strings(t_5) == ["abacaba"]

print("All tests passed successfully!")

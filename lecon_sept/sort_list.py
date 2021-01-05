def sort_ascending(x):
    # вариант 1
    # temp_2 = [j for j in range(len(x)) if x[j] == -1]
    # x.sort()
    # x = [j for j in x if j > 0]
    # for q in temp_2:
    #     x.insert(q, -1)
    # return x

    # вариант 2
    temp_1 = [j for j in x if j != -1]
    temp_1.sort()
    for i in range(len(x)):
        if x[i] == -1:
            temp_1.insert(i, -1)
    return temp_1


test_1 = [-1, 150, 190, 170, -1, -1, 160, 180]
assert sort_ascending(test_1) == [-1, 150, 160, 170, -1, -1, 180, 190]

test_2 = [-1, -1, -1, -1, -1]
assert sort_ascending(test_2) == [-1, -1, -1, -1, -1]

test_3 = [4, 2, 9, 11, 2, 16]
assert sort_ascending(test_3) == [2, 2, 4, 9, 11, 16]

test_4 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
assert sort_ascending(test_4) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

test_5 = [-1]
assert sort_ascending(test_5) == [-1]

print('All tests passed successfully!')

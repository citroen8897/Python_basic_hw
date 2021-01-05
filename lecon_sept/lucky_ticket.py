def is_lucky(ticket_num):
    # Вариант 1 (9 строк)
    # list_1 = [int(i) for i in str(ticket_num)]
    # n = m = 0
    # for a in range(len(list_1) // 2):
    #     n += list_1.pop(0)
    #     m += list_1.pop(-1)
    # if n == m:
    #     return True
    # else:
    #     return False

    # Вариант 2 (7 строк)
    ticket_num = str(ticket_num)
    list_1 = [int(i) for i in ticket_num[:len(ticket_num) // 2]]
    list_2 = [int(j) for j in ticket_num[len(ticket_num) // 2:]]
    if sum(list_1) == sum(list_2):
        return True
    else:
        return False


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print('All tests passed successfully!')

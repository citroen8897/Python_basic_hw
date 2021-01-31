"""
    Алгоритм Евклида. НОД - наибольший общий делитель
    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.
    * разработайте алгоритм, который работает для положительных чисел
"""

numero_un = int(input("Задайте первое число: "))
numero_deux = int(input("Задайте второе число: "))

if numero_un > numero_deux:
    seq_1 = numero_un % numero_deux
    if seq_1 == 0:
        print("НОД введенных чисел равен:", numero_deux)
    while seq_1 != 0:
        t_1 = numero_deux % seq_1
        if t_1 != 0:
            numero_deux = seq_1
            seq_1 = t_1
        else:
            print("НОД введенных чисел равен:", seq_1)
            break

elif numero_deux > numero_un:
    seq_1 = numero_deux % numero_un
    if seq_1 == 0:
        print("НОД введенных чисел равен:", numero_un)
    while seq_1 != 0:
        t_1 = numero_un % seq_1
        if t_1 != 0:
            numero_un = seq_1
            seq_1 = t_1
        else:
            print("НОД введенных чисел равен:", seq_1)
            break

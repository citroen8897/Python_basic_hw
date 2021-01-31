"""
 Программа принимает на ввод 5-ти значное число.
 Заменяет каждую вторую цифру на 0 и выводит результат.
 [in] 12345
 [выход] 10305
 * Если введено не 5-ти значное число
 либо не число обработать и вывести соответствующее сообщение.
"""

number = input("Введите 5-ти значное число: ")
while number.isdigit() != 1 or len(number) != 5 or number[0] == "0":
    number = input("Неверный ввод! Введите 5-ти значное число: ")

number = int(number)
number_un = number % 10
number_dix = (number - number_un) % 100 // 10
number_cent = (number - number_dix * 10 - number_un) % 1000 // 100
number_mille = (
    (number - number_cent * 100 - number_dix * 10 - number_un) % 10000 // 1000
)
number_dix_mille = (
    (
        number
        - number_mille * 1000
        - number_cent * 100
        - number_dix * 10
        - number_un
    )
    % 100000
    // 10000
)

number_modify = (
    str(number_dix_mille) + "0" + str(number_cent) + "0" + str(number_un)
)
print("Введенное число: ", number, "\nМодифицированное число: ", number_modify)

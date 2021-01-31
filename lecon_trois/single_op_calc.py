"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""
while True:

    try:
        user_number_oper = int(
            input("Задайте количество чисел для обработки: ")
        )
        while user_number_oper <= 1:
            user_number_oper = int(
                input("Задайте НЕНУЛЕВОЕ и НЕЕДИНИЧНОЕ количество чисел: ")
            )
    except ValueError:
        print("Ошибочка! Введено не целое число!")
    else:
        user_operation = input("Задайте операцию для выполнения +, -, *, /: ")
        while user_operation not in ("+", "-", "*", "/"):
            user_operation = input(
                "Задайте операцию для выполнения +, -, *, /: "
            )

        try:
            user_numero_travail = int(input("Задайте число для обработки: "))
            result = user_numero_travail
        except ValueError:
            print("Ошибочка! Введено не целое число!")
        else:
            for a in range(user_number_oper - 1):

                if user_operation == "+":
                    user_numero_travail = int(
                        input("Задайте число для обработки: ")
                    )
                    result = result + user_numero_travail

                elif user_operation == "-":
                    user_numero_travail = int(
                        input("Задайте число для обработки: ")
                    )
                    result = result - user_numero_travail

                elif user_operation == "*":
                    user_numero_travail = int(
                        input("Задайте число для обработки: ")
                    )
                    result = result * user_numero_travail

                else:
                    user_numero_travail = int(
                        input("Задайте число для обработки: ")
                    )
                    try:
                        result = result / user_numero_travail
                    except ZeroDivisionError:
                        print("Деление на ноль запрещено!")
                        result = "Результата нет по Вашей вине("

            print(
                "Результат вычисления по заданным параметрам равен: ", result
            )

        plus_travail = input(
            "Желаете выполнить новое вычисление? Введите да/нет: "
        )
        while plus_travail != "да" and plus_travail != "нет":
            plus_travail = input(
                "Желаете выполнить новое вычисление? Введите да/нет: "
            )
        if plus_travail == "нет":
            input("Нажмите любую клавишу для выхода")
            break

# Программа-калькулятор для двух чисел.
# Поддерживаются операции сложения, вычитания, умножения, деления, возведения в степень, деления на цело, извлечение
# корня n-й степени.
# Программа работает с целыми числами, вводимыми пользователем.

try:
    numero_un = int(input("Задайте первое число: "))
    numero_deux = int(input("Задайте второе число: "))
except ValueError:
    print("\nВведены не ЦЕЛЫЕ ЧИСЛА!!!\nПрограмма не выполнена!\n")
else:
    print(
        "\nВозможные операции:\nСуммирование - "
        "+"
        "\nВычитание - "
        "-"
        "\nУмножение - "
        "*"
        "\nДеление - "
        "/"
        ""
        "\nВозведение в степень - "
        "**"
        "\nДеление на цело - "
        "//"
        "\nИзвлечение корня n-й степени - "
        "7"
        "\n"
    )

    user_operation_select = input(
        "Задайте операцию, введением целого числа, согласно инструкции выше: "
    )

    if user_operation_select == "+":
        user_result = numero_un + numero_deux
        print("Сумма чисел", numero_un, "и", numero_deux, "равна", user_result)
    elif user_operation_select == "-":
        user_result = numero_un - numero_deux
        print(
            "Разность чисел", numero_un, "и", numero_deux, "равна", user_result
        )
    elif user_operation_select == "*":
        user_result = numero_un * numero_deux
        print(
            "Произведение чисел",
            numero_un,
            "и",
            numero_deux,
            "равно",
            user_result,
        )
    elif user_operation_select == "/":
        try:
            user_result = numero_un / numero_deux
            print(
                "Частное чисел",
                numero_un,
                "и",
                numero_deux,
                "равно",
                user_result,
            )
        except ZeroDivisionError:
            print("Деление на ноль! Выполнение операции запрещено!")
    elif user_operation_select == "**":
        user_result = numero_un ** numero_deux
        print(
            "Возведение числа",
            numero_un,
            "в степень",
            numero_deux,
            "равно",
            user_result,
        )
    elif user_operation_select == "//":
        try:
            user_result = numero_un // numero_deux
            print(
                "Целое частное чисел",
                numero_un,
                "и",
                numero_deux,
                "равно",
                user_result,
            )
        except ZeroDivisionError:
            print("Деление на ноль! Выполнение операции запрещено!")
    elif user_operation_select == "7":
        user_result = numero_un ** (1 / numero_deux)
        print(
            "Корень",
            numero_deux,
            "-й степени из числа",
            numero_un,
            "равен",
            user_result,
        )
    else:
        print("Операция не выбрана или некорректна.\nПопробуйте позже:)")

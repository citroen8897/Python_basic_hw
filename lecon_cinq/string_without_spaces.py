"""
    Написать программу, которая принимает строку
    и выводит строку без пробелов и ее длину.
    Для удаления пробелов реализовать доп функцию.
"""


def main():
    print("S.P.Q.R.")

    user_string = input("Введите строку: ")
    if len(user_string) == 0:
        return main()

    print(
        f"Строка без пробелов: {delete_spaces(user_string)}\n"
        f"Длина строки с пробелами: {len(user_string)}\n"
        f"Длина строки без пробелов: {len(delete_spaces(user_string))}"
    )


def delete_spaces(s):
    s = s.replace(" ", "")
    return s


if __name__ == "__main__":
    main()

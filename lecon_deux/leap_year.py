# программа проверяет год на "високосность"

try:
    user_year = int(input("Введите год: "))

    if user_year % 4 == 0 and user_year % 100 != 0 or user_year % 400 == 0:
        print(user_year, "високосный год")
    else:
        print(user_year, "невисокосный год")

except ValueError:
    print("Введена некорректная информация. Попробуйте позже:)")

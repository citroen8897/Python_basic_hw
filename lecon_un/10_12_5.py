# пятое упражнение
# площадь и периметр прямоугольного треугольника
print("\nпятое упражнение")

katet_un = float(input("Введите длину первого катета: "))
# тип данных float, что бы расширить возможности для входных данных
katet_deux = float(input("Введите длину второго катета: "))

gipotenouse = (katet_un ** 2 + katet_deux ** 2) ** 0.5
square_tr = (katet_un * katet_deux) / 2
perimetr_tr = katet_un + katet_deux + gipotenouse

print(
    "Площадь заданного треугольника равна:",
    square_tr,
    "кв. ед." "\nПериметр заданного треугольника равен:",
    perimetr_tr,
    "ед.",
)

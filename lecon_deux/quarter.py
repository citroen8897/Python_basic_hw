# По заданным координатам программа определяет четверть нахождения точки в системе координат.

try:
    user_abscise = int(input('Задайте целочисленную координату по оси абсцис: '))
    user_ordinate = int(input('Задайте целочисленную координату по оси ординат: '))

    if user_abscise == 0 and user_ordinate == 0:
        print('Указанная точка является началом системы координат\nи не лежит ни в одной из четвертей системы.')
    elif user_abscise == 0:
        print('Указанная точка лежит на оси абсцис\nи не лежит ни в одной из четвертей системы.')
    elif user_ordinate == 0:
        print('Указанная точка лежит на оси ординат\nи не лежит ни в одной из четвертей системы.')

    elif user_abscise > 0:
        if user_ordinate > 0:
            print('Указанная точка лежит в первой четверти системы координат')
        else:
            print('Указанная точка лежит в четвертой четверти системы координат')
    elif user_abscise < 0:
        if user_ordinate > 0:
            print('Указанная точка лежит во второй четверти системы координат')
        else:
            print('Указанная точка лежит в третьей четверти системы координат')

except ValueError:
    print('Вы некорректно ввели координаты.\nПопробуйте снова:)')

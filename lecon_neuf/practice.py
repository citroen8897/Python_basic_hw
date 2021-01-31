import random
from slow_decorator import time_decorator

# 1. Создайте переменную x, которая равняется 2 в степени 3
x = 2 ** 3

# 2. Прибавьте к x 3
x += 3

# 3. Сгенерируйте список num_list длиной x, из случайных чисел в диапазоне от 1 до x
num_list = [random.randint(1, x) for i in range(x)]

# 4. Выведите на экран числа из списка num_list в обратном порядке
#    (от последнего до первого элемента) через пробел
string_print = ""
for element in num_list[::-1]:
    string_print += f"{element} "
print(string_print)

# 5. Вставьте в средину списка число 11.
temp_1 = len(num_list) // 2
num_list.insert(temp_1 + 1, 11)

# 6. Запишите в файл list_info.txt строчки
#    - количество элементом списка
#    - количество уникальных элементов списка
#    - самое маленькое число списка
#    - сумму чисел списка кратных 3
with open("list_info.txt", "w") as f:
    f.write(str(len(num_list)) + "\n")
    f.write(str(len(set(num_list))) + "\n")
    f.write(str(min(num_list)) + "\n")
    f.write(str(sum(list(filter(lambda j: j % 3 == 0, num_list)))) + "\n")

# 7. Создайте список countries_info из 3 словарей c ключами
#    'country', 'population', 'cities' и заполните их любыми значениями
#    ('country' - строка, 'population' - число, 'cities' - список строк)
countries_info = [
    {
        "country": "Italy",
        "population": 81,
        "cities": ["Rome", "Milano", "Torino"],
    },
    {
        "country": "France",
        "population": 75,
        "cities": ["Paris", "Nantes", "Lans"],
    },
    {
        "country": "Russia",
        "population": 145,
        "cities": ["Moscow", "St. Petersburg", "Vladivostok"],
    },
]

# 8. Отсортируйте в каждом словаре cities по длине строк в порядке убывания
for element in countries_info:
    print(list(reversed(sorted(element["cities"], key=lambda y: len(y)))))

# 9. Отсортируйте список словарей countries_info
#    по ключу 'population' в порядке возрастания
print(sorted(countries_info, key=lambda q: q["population"]))

# 10. Напишите функцию create_country_info, которая принимает 3 параметра
#     country, population и cities
#     и возвращает словарь типа
#     {'country': 'USA', 'population': 123, 'cities': ['New York', 'Los Angeles', 'Portland']}


@time_decorator
def create_country_info(country, population, cities):
    dict_info_country = {
        "country": country,
        "population": int(population),
        "cities": cities,
    }
    return dict_info_country


print(
    create_country_info(
        "Italy",
        "81",
        ["Rome", "Torino", "Milano", "Bergamo", "Palermo", "Triest"],
    )
)

# 11. Создайте словарь с помощью функции create_country_info
#     и вставьте его в начало списка countries_info
temp_2 = create_country_info(
    "Turkmenistan", "6", ["Ashgabat", "Turkmenabat", "Daşoguz"]
)
countries_info.insert(0, temp_2)
print(countries_info)

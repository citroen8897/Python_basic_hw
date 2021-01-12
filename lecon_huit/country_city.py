"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит.
    Покрыть функцию тестами.
    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
"""

data = {
    'Ukraine': ['Kiev', 'Kharkiv', 'Odesa', 'Dnipro'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse'],
    'Austria': ['Vienna', 'Graz', 'Linz', 'Salzburg'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Frankfurt']
}


def get_country(city, data):
    for k, v in data.items():
        if city in v:
            return k


assert get_country('Kharkiv', data) == 'Ukraine'
assert get_country('Salzburg', data) == 'Austria'
assert get_country('Paris', data) == 'France'
assert get_country('Berlin', data) == 'Germany'
print('All tests passed successfully!')


def groupping(data):
    list_temp = []
    for k, v in data.items():
        d_1 = {'country': k, 'capital': v[0], 'cities': v[1:]}
        list_temp.append(d_1)
    return list_temp


for line in groupping(data):
    print(line)

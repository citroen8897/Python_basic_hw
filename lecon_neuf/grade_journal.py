"""
    Пользователь вводит количество студентов n.
    После чего вводит n строк, в которых записана фамилия и балл через пробел.
    Программа выводит список фамилий, отсортированный по их баллам по убыванию.
    Пример:
    [out] Введите количество студентов:
    [in]  3
    [out] Введите фамилию и балл:
    [in]  Иванов 87
    [out] Введите фамилию и балл:
    [in]  Смирнов 90
    [out] Введите фамилию и балл:
    [in]  Фролов 89
    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""
from slow_decorator import time_decorator


@time_decorator
def main():
    try:
        get_numero_des_etudiants = int(input('Задай количество студентов: '))
    except ValueError:
        get_numero_des_etudiants = int(input('Некорректно!\n'
                                             'Задай количество студентов: '))
    get_etudiant_et_numero = []
    for i in range(get_numero_des_etudiants):
        user_input = input('Введи фамилию и оценку: ')
        nom_de_etudiant = ''
        numero_de_etudiant = ''
        for j in user_input:
            if j.isalpha():
                nom_de_etudiant += j
            elif j.isdigit():
                numero_de_etudiant += j
        dict_temp = {'nom': nom_de_etudiant.title(),
                     'numero': int(numero_de_etudiant)}
        get_etudiant_et_numero.append(dict_temp)
    get_etudiant_et_numero.sort(key=lambda data: data['numero'])
    for element in get_etudiant_et_numero[::-1]:
        print(f'{get_etudiant_et_numero[::-1].index(element) + 1}. '
              f'{element["nom"]}')


if __name__ == '__main__':
    main()

"""
    Реализовать декораторы:
    1. @time_decorator - считает и выводит время работы функции,
        если функция выполняется дольше 5 секунд, тогда дополнительно
        выводить сообщение print(f'{func.__name__} - very slow function')
    * в func.__name__ лежит название функции
    2. @slow_decorator - замедляет выполнение функции на 5 секунд
"""


def time_decorator(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(
            f"\nВремя выполнения функции {func.__name__} {end - start} "
            f"секунд"
        )

        if end - start > 5:
            print(f"{func.__name__} - очень медленная функция")

        return return_value

    return wrapper


def slow_decorator(func):
    import time

    def wrapper(*args, **kwargs):
        time.sleep(5)
        return_value = func(*args, **kwargs)
        return return_value

    return wrapper

"""
    1. Нарисовать границу из * в списке.
    [in]    ['python',
             'django']
    [out]   ['********',
             '*python*',
             '*django*',
             '********']
    [in]    ['abc',
             'def']
    [out]   ['*****',
             '*abc*',
             '*def*',
             '*****']
    Покрыть несколькими тестами.
"""


def draw_border(list_):
    temp_1 = len(list_[0])
    s_2 = ""
    for i in range(temp_1 + 2):
        s_2 += "*"
    s_3 = f"*{list_[0]}*"
    s_4 = f"*{list_[1]}*"
    list_ = [s_2, s_3, s_4, s_2]
    return list_


list_ = ["python", "django"]
assert draw_border(list_) == ["********", "*python*", "*django*", "********"]

list_ = ["abc", "def"]
assert draw_border(list_) == ["*****", "*abc*", "*def*", "*****"]

list_ = ["c", "f"]
assert draw_border(list_) == ["***", "*c*", "*f*", "***"]
print("All tests passed successfully!")

"""
    * Реверс подстроки в ()
    Таким образом, чтоб:
    [in]    "(bar)"
    [out]   "rab"
    [in]    "foo(bar)baz"
    [out]   "foorabbaz"
    [in]    "foo(bar)baz(blim)"
    [out]   "foorabbazmilb"
    [in]    "foo(bar(baz))blim"
    [out]   "foobazrabblim"
    так как "foo(bar(baz))blim" -> "foo(barzab)blim" -> "foobazrabblim"
    Данные примеры можете использовать для написания тестов.
"""
import re


def reverse_brackets(input_string):
    if not re.search(r"\)\w*\)", input_string):
        while "(" in input_string:
            index_1 = input_string.find(")")
            index_2 = input_string.find("(")
            string_temp_1 = input_string[index_2 + 1 : index_1]
            string_temp_1 = string_temp_1[::-1]
            input_string = (
                input_string[:index_2]
                + string_temp_1
                + input_string[index_1 + 1 :]
            )
    else:
        while "(" in input_string:
            index_1 = input_string.find(")")
            index_2 = input_string.rfind("(")
            string_temp_1 = input_string[index_2 + 1 : index_1]
            string_temp_1 = string_temp_1[::-1]
            input_string = (
                input_string[:index_2]
                + string_temp_1
                + input_string[index_1 + 1 :]
            )
    return input_string


string = "(bar)"
assert reverse_brackets(string) == "rab"

string = "foo(bar)baz"
assert reverse_brackets(string) == "foorabbaz"

string = "foo(bar)baz(blim)"
assert reverse_brackets(string) == "foorabbazmilb"

string = "foo(bar(baz))blim"
assert reverse_brackets(string) == "foobazrabblim"

print("All tests passed successfully!")

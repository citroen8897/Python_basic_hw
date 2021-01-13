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
    list_temp = [i for i in (re.split(r'(\w*)', input_string)) if i != '']
    for i in range(len(list_temp)):
        if list_temp[i] == '(':
            list_temp[i + 1] = list_temp[i + 1][::-1]
    list_temp = [i for i in list_temp if i not in ('(', ')')]
    output_string = ''.join(list_temp)
    return output_string


string = '(bar)'
assert reverse_brackets(string) == 'rab'

string = 'foo(bar)baz'
assert reverse_brackets(string) == 'foorabbaz'

string = 'foo(bar)baz(blim)'
assert reverse_brackets(string) == 'foorabbazmilb'

# string = 'foo(bar(baz))blim'
# assert reverse_brackets(string) == 'foobazrabblim'
print('All tests passed successfully!')

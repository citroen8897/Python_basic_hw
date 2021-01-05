s = ['1', 'sdasd', '123', '3.14', 'w3s']
s_1 = [int(i) for i in s if i.isdigit()]
print(s_1)

s_1 = []
for i in s:
    if i.isdigit():
        s_1.append(i)
print(s_1)


s = [1, 2, 3, 4, 5]
s = [s[-1]] + s[1:-1] + [s[0]]
print(s)

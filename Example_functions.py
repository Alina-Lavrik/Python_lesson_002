# Функции

''' def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))  # !!!!!
print(new_string('!'))     # !!!
print(new_string(4))       # 12 '''

''' def concatenatio(*params):
    res: str = ""          # работаем со строкой
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))   # asdw
print(concatenatio('a', '1'))             # a1
print(concatenatio(1, 2, 3, 4))           # TypeError: ... '''

def concatenatio(*params):
    res: int = 0         # работаем c числами
    for item in params:
        res += item
    return res

print(concatenatio(1, 2, 3, 4))   # 10
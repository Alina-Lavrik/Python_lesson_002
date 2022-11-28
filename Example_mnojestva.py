# Множества

'''colors = {'red', 'green', 'blue'}
print(type(colors))   # типо данных множества <class 'set'>
print(colors)   # {'green', 'blue', 'red'}

colors.add('gray')
print(colors)  # {'gray', 'blue', 'red', 'green'}

colors.remove('red')
print(colors)  # {'green', 'blue', 'gray'}

colors.discard('red')
print(colors)   # {'blue', 'green', 'gray'}

colors.clear()  # очистить множество
print(colors)   # set() '''

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()    # c = {1, 2, 3, 5, 8}
# print(c) 
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)
i = a.intersection(b)  # i = {8, 2, 5}
# print(i) 
dl = a.difference(b)  # dl = {1, 3}
# print(dl)
dr = b.difference(a) # dr = {13, 21}
# print(dr)

q = a \
    .union(b) \
    .difference(a.intersection(b))
# print(q)    
# {1, 21, 3, 13}

# Неизменяемые множества

s = frozenset(a)



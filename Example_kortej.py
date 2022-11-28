# Кортеж

a = (3, 4)
print(a) # (3, 4)
print(a[0]) # 3
print(a[-1]) # 4 - выводит последний элемент

b = (3, 84, 22, 99, 150)
print(b[-2]) # 99

c = (3, 84, 22, 99, 150)
for item in c:
    print(item)
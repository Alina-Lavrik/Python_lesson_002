# Списки

''' list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)
print()
for e in list2:
    print(e)
list1[0] = 123
list2[1] = 333
print()
for e in list1:
    print(e)
print()
for e in list2:
    print(e)

123
333
3
4
5

123
333
3
4
5'''

''' list1 = [1, 2, 3, 4, 5]
print(len(list1))
print(list1.pop())  # метод pop извлекает последний элемент из списка
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)


5
5
[1, 2, 3, 4]
4
[1, 2, 3]
3
[1, 2]  '''

'''list1 = [1, 2, 3, 4, 5]

print(list1.pop(2))   # удалить конкретный элемент
print(list1)
# 3
# [1, 2, 4, 5] '''

'''list1 = [1, 2, 3, 4, 5]
print(list1.insert(2, 11))   #  вставить между 2 и 3 число 11
print(list1)
# None
# [1, 2, 11, 3, 4, 5] '''



list1 = [1, 2, 11, 3, 4, 5]
print(list1.append(11))  # добавить в конец списка
print(list1)
# None
# [1, 2, 11, 3, 4, 5, 11]

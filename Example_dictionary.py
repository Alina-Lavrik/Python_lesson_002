# Словари

dictionary = {}  # присвоить пустое значение
dictionary = \
    {
        'up' : '|',
        'left' : '<-',
        'down' : '|',
        'right' : '->'
    }
print(dictionary)  # {'up': '|', 'left': '<-', 'down': '|', 'right': '->'}
print(dictionary['left']) # <-
del dictionary['left'] # удаление элемента

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))
# up: |
# down: |
# right: ->


# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)
# up
# left
# down
# right

for k in dictionary.values():
    print(k)
# |
# <-
# |
# -> 


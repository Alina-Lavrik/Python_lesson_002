'''colors = ['red', 'green', 'blue123']
data = open('file.txt', 'a')             # созд тестовую переменную дата и связываем ее с тестовым файлом, 
                                         # file.txt - путь к файлу, a - мод, с которым будем работать
                                         # a - дозапись, w - запись, r - чтение
# data.writelines(colors)  # разделителей не будет
data.write('LINE 121\n')    # \n - переход на новую строку
data.write('LINE 131\n')
data.close() '''

# with open('file.txt', 'a') as data:
#    data.write('line 1111\n')
#    data.write('line 2222\n')  # не нужно вызывать закрытие файла

path = 'file.txt'   # создадим путь к папочке
data = open(path, 'r')   # откроем в режиме чтения
for line in data:   # при помощи цикла пробежимся по файлу и считаем все строки
    print(line)
data.close()       # после того, как закончили чтение разорвем связь с файлом

exit()

import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('Создаем папки от 1 до 9: ')
os.getcwd()
for i in range(1, 10):
    try:
        os.mkdir('dir_' + str(i))
    except:
        print('Папка ' + 'dir_' + str(i) + ' уже существует')
print(os.listdir())
stoppy = input('Если вы хотите удалить пустые папки? - нажмите клавишу "Y" :')
if stoppy.upper() == 'Y':
    for x in range(1, 10):
        os.rmdir('dir_' + str(x))

print(os.listdir())
print('Конец выполнения программы')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

dir_list = os.listdir()
print('Выводим список папок текущей директории: ')
for i in dir_list:
    if os.path.isdir(i) == True:
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

os.getcwd()
file = open('DZ_lesson_five_easy.py', 'rb')
file1 = open('COPY_DZ_lesson_five_easy.py', 'wb')
new_file = file1.write(file.read())
file.close()
file1.close()

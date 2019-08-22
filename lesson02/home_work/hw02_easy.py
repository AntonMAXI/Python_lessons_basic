# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruit_list = ['apple', 'banana', 'piapple', 'apricot', 'lemon', 'kiwi']
print(type(fruit_list))
print('1.{0:>10}\n2.{1:>10}\n3.{2:>10}\n4.{3:>10}\n5.{4:>10}\n6.{5:>10}'.format(*fruit_list))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

surname = list('maximov')
print(surname)
name = list('anton')
print(name)
i = 0
while int(i) < len(surname):
    for item in name:
        if item in surname:
                surname.remove(item)
                i += 1
        else:
                i += 1
print('Delete coincidence in words')
print(surname)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('Next level')
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('List is ', list_numbers)
for itm in range(len(list_numbers)):
    if list_numbers[itm] % 2 == 0:
        list_numbers[itm] /= 4
    else:
        list_numbers[itm] *= 2
print(list_numbers)

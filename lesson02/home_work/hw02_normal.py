# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
import random

list_numbers = [2, -5, 8, 9, -25, 25, 4]
new_list_numbers = []
for itm in list_numbers:
    if itm > 0 and math.sqrt(itm) % 1 == 0:
        new_list_numbers.append(int(math.sqrt(itm)))
print(new_list_numbers)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

dict_num = {'01': 'first', '02': 'second', '03': 'third',
            '04': 'fourth', '05': 'fifth', '06': 'sixth',
            '07': 'seventh', '08':'eighth', '09': 'ninth',
            '10': 'tenth', '11': 'eleventh', '12': 'twelfth',
            '13': 'thirteenth', '14': 'fourteenth', '15': 'fifteenth',
            '16': 'sixteenth', '17': 'seventeenth', '18': 'eighteenth',
            '19': 'nineteenth', '20': 'twentieth', '21': 'twenty first',
            '22': 'twenty second', '23': 'twenty third', '24': 'twenty fourth',
            '25': 'twenty fifth', '26': 'twenty sixth', '27': 'twenty seventh',
            '28': 'twenty eighth', '29': 'twenty ninth', '30': 'thirtieth',
            '31': 'thirtieth first'}
dict_month = {'01': ' january', '02': ' february', '03': ' march',
            '04': ' april', '05': ' may', '06': ' june',
            '07': ' july', '08': ' august', '09': ' september',
            '10': ' october', '11': ' november', '12': ' december',
              }
i=0
while i < 10:
    try:
        date = input('Insert date in format dd.mm.yyyy:').split('.')
        print('{0}{1} {2}'.format(dict_num[date[0]], dict_month[date[1]], date[2] + ' year'))
        i+=1
        break
    except KeyError:
        print('Некорректная дата, попробуйте ещё раз.')
        i+=1

        
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

list_rand_numbers = []
elem = input('Insert quantity numbers')
i = 0
while i < int(elem):
    list_rand_numbers.append(random.randint(-100, 100))
    i+=1
print(list_rand_numbers)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
print('Source list : ', lst)
lst2 = []
lst3 = []
i = 0
for itm in lst:
    if itm not in lst2:
        lst2.append(itm)
print('Non-repeating elements of the source list : ', lst2)
for itm in lst:
    if lst.count(itm) == 1:
        lst3.append(itm)
print('Items in the source list that have no repetitions : ',lst3)

# задание-1:
# напишите функцию, возвращающую ряд фибоначчи с n-элемента до m-элемента.
# первыми элементами ряда считать цифры 1 1

n = int(input('First num : '))
m = int(input('Second num : '))

def fibonacci(n,m):
    dict_1 = {}
    k1 = k2 = 1
    for i in range(1,m + 1):
        dict_1[i] = [k1, k2]
        k1 = k2 + k1
        k2 = k1 + k2

    for key in dict_1.keys():
        if int(key) >= int(n):
            print(dict_1[key])

fibonacci(n,m)

# задача-2:
# напишите функцию, сортирующую принимаемый список по возрастанию.
# для сортировки используйте любой алгоритм (например пузырьковый).
# для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for itm in range(len(origin_list) - n):
            if origin_list[itm] > origin_list[itm + 1]:
                origin_list[itm], origin_list[itm + 1] = origin_list[itm + 1], origin_list[itm]
        n += 1

    return print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
sort_to_max([2, 10, 12, 2.5, 20, 11, 4, 4, 0])





# задача-3:
# напишите собственную реализацию стандартной функции filter.
# разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, lis):
    lis2 = []
    for x in lis:
        if func(x):
            lis2.append(x)
    return lis2
a = [5, 25, 15, 3, 3, -10]
print(my_filter(lambda x: x % 5 == 0, a))

# задача-4:
# даны четыре точки а1(х1, у1), а2(x2 ,у2), а3(x3 , у3), а4(х4, у4).
# определить, будут ли они вершинами параллелограмма.

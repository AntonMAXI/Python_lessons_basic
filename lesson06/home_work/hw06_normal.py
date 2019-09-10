# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# class School():

# def __init__(self, name=None, surname=None):
#
#


class Students():
    def __init__(self, fam, name=None, otch=None):
        self.fam = fam
        self.name = name
        self.otch = otch

    def sp_students(self):
        return self.fam + " " + self.name + " " + self.otch


class Claz():
    def __init__(self, one_claz, two_claz, three_claz):
        self.one_claz = one_claz
        self.two_claz = two_claz
        self.three_claz = three_claz

    def classes(self):
        return self.one_claz + " " + self.two_claz + " " + self.three_claz


class Teach():
    def __init__(self, fam, name=None, otch=None, klass=None, lit_klass=None):
        self.fam = fam
        self.name = name
        self.otch = otch
        self.klass = klass
        self.lit_klass = lit_klass

    def teacher(self):
        return self.fam + " " + self.name + " " + self.otch


classes = [Claz('1A', '2A', '3A')]

stud = [Students('Maximov', 'Anton', 'Vasylievich'),
        Students('Maximov', 'Mihail', 'Antonovich'),
        Students('Maximov', 'Vasilyi', 'Dmitrievich')]

teachers = [Teach('Maximov', 'Abraham', 'Asikovich'),
            Teach('Maximov', 'HaudyHO', 'Jonovich'),
            Teach('Maximov', 'Andrey', 'Gorbatovich')]

for itm in classes:
    print(itm.classes())
for itm in stud:
    print(itm.sp_students())
for itm in teachers:
    print(itm.teacher())

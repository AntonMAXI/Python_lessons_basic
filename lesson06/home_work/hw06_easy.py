# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Treug():

    def __init__(self, A=None, B=None, C=None):
        self.A = A
        self.B = B
        self.C = C
        self.st_AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        self.st_AC = math.sqrt((self.C[0] - self.A[0]) ** 2 + (self.C[1] - self.A[1]) ** 2)
        self.st_BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)
        print('Точки треуголника заданы')

    if __name__ == '__main__':
        @property
        def vis(self):
            visot = (self.st_AB + self.st_AC + self.st_BC) * 1 / 2
            return float(visot)

    if __name__ == '__main__':
        @property
        def per(self):
            perimetr = self.st_AB + self.st_AC + self.st_BC
            return float(perimetr)

    if __name__ == '__main__':
        @property
        def plo(self):
            plosh = 1 / 2 * (self.st_AB * ((self.st_AB + self.st_AC + self.st_BC) * 1 / 2))
            return float(plosh)


Tr = Treug((2, 4), (4, 8), (6, 1))
print(Tr.A)
print(Tr.B)
print(Tr.C)
print('Длина стороны АВ равна :')
print(Tr.st_AB)
print('Длина стороны АС равна :')
print(Tr.st_AC)
print('Длина стороны ВС равна :')
print(Tr.st_BC)
print('Высота равна :')
print(Tr.vis)
print('Периметр равен :')
print(Tr.per)
print('Площадь равна :')
print(Tr.plo)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


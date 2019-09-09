# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Treug():

    def __init__(self, A=None, B=None, C=None):
        self.A = A
        self.B = B
        self.C = C

        print('Точки треуголника заданы')

    def dlina_AB(self):
        self.st_AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        print('Длина стороны АВ равна :')
        return self.st_AB

    def dlina_AC(self):
        self.st_AC = math.sqrt((self.C[0] - self.A[0]) ** 2 + (self.C[1] - self.A[1]) ** 2)
        print('Длина стороны АС равна :')
        return self.st_AC

    def dlina_BC(self):
        self.st_BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)
        print('Длина стороны ВС равна :')
        return self.st_BC

    def vis(self):
        visot = (self.st_AB + self.st_AC + self.st_BC) * 1 / 2
        print('Высота равна :')
        return float(visot)

    def per(self):
        perimetr = self.st_AB + self.st_AC + self.st_BC
        print('Периметр равен :')
        return float(perimetr)

    def plo(self):
        plosh = 1 / 2 * (self.st_AB * ((self.st_AB + self.st_AC + self.st_BC) * 1 / 2))
        print('Площадь равна :')
        return float(plosh)

Tr = Treug((2, 4), (4, 8), (6, 1))
print(Tr.A)
print(Tr.B)
print(Tr.C)
print(Tr.dlina_AB())
print(Tr.dlina_AC())
print(Tr.dlina_BC())
print(Tr.vis())
print(Tr.per())
print(Tr.plo())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Ravtrap():

    def __init__(self, A, B, C, D, do_AB=None, do_CD=None, do_AD=None):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.do_AB = do_AB
        self.do_CD = do_CD
        self.do_AD = do_AD

    @property
    def checking(self):
        self.do_AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        self.do_CD = math.sqrt((self.D[0] - self.C[0]) ** 2 + (self.D[1] - self.C[1]) ** 2)
        self.do_BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)
        self.do_AD = math.sqrt((self.D[0] - self.A[0]) ** 2 + (self.D[1] - self.A[1]) ** 2)
        if self.do_AB == self.do_CD or self.do_BC == self.do_AD:
            self.s = f'{"Трапеция равнобедренная"}'
        else:
            self.s = f'{"Трапеция не равнобедренная"}'
        return self.s

    def H(self):
        self.H = math.sqrt(self.do_AB ** 2 - (
                ((self.do_BC - self.do_AD) ** 2 + self.do_AB ** 2 - self.do_CD ** 2) / 2 * (
                self.do_BC - self.do_AD)) ** 2)
        return float(self.H)

    def AB(self):
        AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        return AB

    def BC(self):
        BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)
        return BC

    def CD(self):
        CD = math.sqrt((self.D[0] - self.C[0]) ** 2 + (self.D[1] - self.C[1]) ** 2)
        return CD

    def AD(self):
        AD = math.sqrt((self.D[0] - self.A[0]) ** 2 + (self.D[1] - self.A[1]) ** 2)
        return AD

    def perim(self):
        per = self.do_AB + self.do_CD + self.do_AD + self.do_BC
        return per

    def plosh(self):
        plo = 4 * ((self.do_BC + self.do_AD) / 2)
        return plo


rt = Ravtrap((0, 2), (0, 7), (2, 5), (2, 4))
print('Проверка трапеции : ')
print(rt.checking)
print('Периметр трапеции равен :')
print(rt.perim())
print('Высота трапеции равна :')
print(rt.H())
print('Площадь трапеции равна :')
print(rt.plosh())

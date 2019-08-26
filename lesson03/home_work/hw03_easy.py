# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    degree = 10 ** (ndigits + 1)
    new_state = int(number * degree)
    i = 1
    while (degree - 1) // 10 > 0:
        decimal_value = (new_state % 10 ** i) // (10 ** (i - 1))
        i += 1
        if decimal_value <= 5:
            break
        elif (decimal_value < 9) and (decimal_value > 5):
            new_state += (10 - decimal_value)
            break
        elif decimal_value == 9:
            new_state += (10 - decimal_value)
        degree //= 10
    return new_state / 10 ** (ndigits + 1)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    l_tick = []

    for x in str(ticket_number):
        l_tick.append(x)
        first = (l_tick[:len(l_tick) // 2])
        second = (l_tick[len(l_tick) // 2:])

    for i in range(len(first)):
        first[i] = int(first[i])
    sum_1 = sum(first)

    for i in range(len(second)):
        second[i] = int(second[i])
    sum_2 = sum(second)

    if sum_1 == sum_2:
        return 'LUCKY!!!!'
    else:
        return 'NO GOOD'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(4367514747))
print(lucky_ticket(436751456457457))
print(lucky_ticket(2222222222222222))

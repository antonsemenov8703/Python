

# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))


# if a == b*b : #or b == a**2
#     print(f'Число {a} является квадратом числа {b}')
# elif b == a**2:
#     print(f'Число {b} является квадратом числа {a}')
# else:
#     print('Ни одно из чисел не является квадратом другого')

print('Да' if a**2==b or b**2==a else 'Нет')
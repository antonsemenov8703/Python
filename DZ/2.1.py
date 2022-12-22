# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = input("Введите вещественное число: ")
number_list = []
result = 0
number_list = number
for i in range(len(number_list)):
    if number_list[i]!='.':
        result += int(number_list[i])
print(result)

# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

from random import randrange
import math


def random_number_list(count, list_name, number_range):
    list_name = []
    for i in range(count): # кол-во элементов
        temp = randrange(number_range) # величина элементов random(0,count)
        list_name.append(temp)
    return list_name

def sum_even_index(list_name):
    sum = 0
    for i in range(int(math.ceil(len(list_name)/2))): 
        sum += list_name[2*i] 
    return sum


count = int(input("Задайте кол-во произвольных чисел в списке: "))
list_1 = []
new_list = random_number_list(count,list_1,10)
print("Список из произвольных чисел: ", new_list) 
print("Сумма элементов на нечёиных позициях: ", sum_even_index(new_list))
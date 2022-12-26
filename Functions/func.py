
# Задаёт список, состоящий из произвольных чисел (в диапазоне number_range), 
# количество задаёт пользователь (count).

from random import randrange
def random_number_list(count, list_name, number_range):
    list_name = []
    for i in range(count): # кол-во элементов
        temp = randrange(number_range) # величина элементов random(0,count)
        list_name.append(temp)
    return list_name


# Ищет сумму элементов на чётных индексах. 
import math

def sum_even_index(list_name):
    sum = 0
    for i in range(int(math.ceil(len(list_name)/2))): 
        sum += list_name[2*i] 
    return sum



# Перевод из 10 в 2 систему счисления

def decimal_to_binary(num_10):
    num_2 = []
    while num_10:
        num_2.append(num_10%2)
        num_10 //=2
    num_2.reverse()
    return num_2
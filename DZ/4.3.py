# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


# модуль collections
# choice a не sample

# choice returns a random item from a list, tuple, or string. Syntax: random

import random
from random import randrange

my_list = []
new_list = []
list_of_removed = []

def random_number_list(count, number_range):
    list_name = []
    for i in range(count): # кол-во элементов
        temp = randrange(number_range) # величина элементов random(0,count)
        list_name.append(temp)
    return list_name

num = int(input("Введите число: "))
if num <= 0: print("Не корректное число!")
else:
    my_list = random_number_list(num, 10)
    # my_list = [1, 2, 3, 1, 2, 4, 2, 5, 2, 5, 0]
    # my_list = [2, 9, 2, 6, 6, 9, 6, 8, 8, 7]
    # my_list = [3, 3, 3, 3, 3]
    print(my_list)

    for i in range (len(my_list)):
        if my_list[i] not in new_list and my_list[i] not in list_of_removed:
            new_list.append(my_list[i])
        elif my_list[i] in new_list  :
            list_of_removed.append(my_list[i])
            new_list.remove(my_list[i])

    print(new_list)


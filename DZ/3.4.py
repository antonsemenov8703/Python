# 4. Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random 

def random_float_list(count, list_name, number_range):
    list_name = []
    for i in range(count):
        temp = round(random.uniform(1, number_range),2) 
        list_name.append(temp)
    return list_name


def comp_fract_part(list_name):
    max_index = 0
    min_index = 0 
    dif = 0
    max_num = int(round(list_name[0]%1, 2)*100)
    min_num = int(round(list_name[0]%1, 2)*100)
    for i in range(len(list_name)):
        if int((round(list_name[i]%1, 2))*100) > max_num:
            max_num = int((round(list_name[i]%1, 2))*100)
            max_index = i
        elif int((round(list_name[i]%1, 2))*100) < min_num:
            min_num = int((round(list_name[i]%1, 2))*100)
            min_index = i
        dif = round((list_name[max_index] - list_name[min_index])%1, 2)
    print ("max = ", max_num, ", min = ", min_num, ", diff = ", dif)
   

num = int(input("Введите кол-во чисел в списке: "))
list_1 = []
list_2 = random_float_list(num, list_1, 10)
print(list_2)
comp_fract_part(list_2)

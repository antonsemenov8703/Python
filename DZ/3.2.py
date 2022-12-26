# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randrange

def random_number_list(count, list_name, number_range):
    
    list_name = []
    for i in range(count): 
        temp = randrange(number_range) 
        list_name.append(temp)
    return list_name

def product_num (list_name):
    
    list_output = []
    m = int(len(list_name))
    for i in range(int(m/2)):
        sum = new_list[i] * new_list[m-1-i] 
        list_output.append(sum)
    if m%2 != 0:
        list_output.append(new_list[int(m/2)]) 
    print (list_output)


count = int(input("Введите длину списка: "))
list_1 = []
new_list = random_number_list(count,list_1, 10)
print(new_list)
product_num(new_list)

# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]


# lst = [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# for i in range (1,len(lst)):
#     if lst[i] > lst[i-1]:
#         print(lst[i])

# Сначала сделал постарому, потом переделал в list comp

lst = [15, 16, 2, 3, 1, 7, 5, 4, 10]
print(lst)
lst=[lst[i] for i in range(1,len(lst)) if lst[i] > lst[i-1]]
print(lst)



# # из разбора на семинаре:

# from random import sample

# def more_then(num):
#     my_list = sample(range(num*3),num)
#     print(my_list)
#     return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num-1]]

# print(more_then(int(input())))


# from random import randint

# def more_then (num):
#     original_list = [randint(0, 1000) for _ in range (num)]
#     print (original_list)
#     return [num for i, num in enumerate (original_list[1:]) if num > original_list[i]]

# more_then(10)
# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# m = number_list.len
for i in range(len(number_list)):
    import random 
    a = random.randint(0,9)
    b = random.randint(0,9)
    temp = number_list[a]
    number_list[a] = number_list[b]
    number_list[b] = temp
print(number_list)



# Другой вариант из разбора на семинаре

from random import randrange

num = int(input)
nums_list = list(range(num))

print(num_list)

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num) # присваеваем рандомные значения
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1] # меняем местами значения 

print(nums_list)

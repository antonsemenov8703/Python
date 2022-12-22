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


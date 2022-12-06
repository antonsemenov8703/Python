# 1. Найти максимальное из пяти чисел.


# lst = []
# for i in range(5):
#     lst.append(int(input('Введите число ')))
# a = 0
# for i in lst:
#     if i > a:
#         a = i
# print (a)


# a = [3, 4, 9, 5, 1]
# print( "max =", max(a))



# num = [1, 4, 8, 7, 5]
# max_ = num[0]

# for i in num[1:]:
#     if i > max_:
#         max_ = i

# print(max_)


# number = int(input('Введите какое кол-во чисел будем сравнивать:'))
# lst = []
# for i in range(number):
#     lst.append(int(input('Введите число ')))
# max_value = lst[0]
# for i in lst:
#     if i > max_value:
#         max_value = i
# print (f'Максимальное из введёных чисел {lst} - это {max_value}')



number = int(input('Введите какое кол-во чисел будем сравнивать:'))
lst = []
for i in range(number):
    lst.append(int(input('Введите число ')))
print (f'Максимальное из введёных чисел {lst} - это {max(lst)}')


# lst = [int(i) for i in input().split()] # ввод списка в строку ОГРОМНЫЙ плюс в том, что можно вводить любое кол-во элементов

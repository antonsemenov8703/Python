# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

N = int(input("Введете число N: "))
position_one = int(input("Введете первое число: "))
position_two = int(input("Введете второе число: "))
number_list = []

if N > 0:
    for i in range(-N, N+1):
        number_list.append(i)
else: print("N - should be > 0")

if 0 < position_one < (2*(N+1)) and 0 < position_two < (2*(N+1)):
    a = number_list[(position_one - (2*(N +1)) )]
    b = number_list[(position_two - (2*(N +1)) )]
    result = a*b
    print(N)
    print(number_list)
    print("Произведение элементов", position_one, " и ",position_two, " = ", result  )
else: print("There are no values for these indexes!")



# вариант решения на семинаре
# тут плюс в том, что используется длина списка, к не математическое вычисление длины как написано у меня

num = int(input)
n_1 = int(input)
n_2 = int(input)

num_list = list(range(-num, num +1))  # таким образом мы можем заполнить список без использования цикла


print(num_list)
len_list = len(num_list)

if len_list >= n_1 > 0 and len_list >= n_2 > 0:
    print(num_list[n_1 - 1] * num_list[n_2 - 1])
else:
    print("There are no values for these indexes!")


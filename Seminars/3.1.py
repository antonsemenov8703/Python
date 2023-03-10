# Задача 1
# Задайте список, состоящий из произвольных чисел,
# кол-во задаёт пользователь. Написать программу,
# определяющую присутствует ли в заданном списке число,
# полученное от пользователя.

# Воспользуемся функцией sample из random - функция принимает кол-во и то что мы ищем - т.е. 2 парамметра
# sample берёт на вход последовательность чисел и сколько мы хотим из этой последовательности взять 
# при том, эти значения не будут повторяться

from random import sample # это мы подключили библиотеку, чтобы пользоваться функцией sample 

def num_find (len_list, number):
    
    new_list = sample (range(1,len_list*2), k = len_list) # *2 чисто для того, чтобы была возможность ввести число, которого может не быть в списке. в длине 10 число от 1-10 мы всегда угадаем, а вот из 20 есть шанс не угадать.
    print(new_list)

    if number in new_list: # функция, которая смотрит есть ли значение в списке - и возвращает true or false
        return "Yes" # Не используем else, т.к. после return уже не сработает else , функция завершится
    return "No"
print(num_find(int(input("Введите длину: ")), int(input("Введите число: "))))
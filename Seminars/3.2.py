# Задача 2. 
# Задайте список, состоящий из произвольных слов, 
# количество задаёт пользователь.
# Напишите программу, которая определит индекс 
# второго вхождения строки в списке
# либо сообщит, что её нет.

from random import sample

# # sample
# def random_words_list(count, word="abc"): # count - кол-во повторяющихся слов в нашем списке, word - это слово из которого будем формировать набор значений
#     my_list = []
#     for i in range(count):
#         temp = sample(word, k=3)  # переменная в которую записываем слово вытянутое по одной неповторяющейся букве из слова word(abc) в кол-ве 3 букв
#         my_list.append("".join(temp)) # мы методом join (чтобы был список) складываем  в my_list буквы (temp) убирая пробелы " ".
#     return my_list

# def index_find(word_2, list_2): # функция для поиска второго вхождения
# # list не нужно писать с []  т.к. python понимает, что это список 
#     if word_2 in list_2 and list_2.count(word_2)>1:  # если слово входит в список # count - функция, которую мы применяем к list_2
#         index_1 = list_2.index(word_2)  # метод index, которому передаём искать word_2 , index_1 - это переменная в которое записываем кол-во повторений слов    
#         print(list_2.index(word_2,index_1+1)) # тут выводим второе вхождение, по этому пишем +1, 
#     else:
#         print(-1)

# list_1 = random_words_list(int(input("Введите значение: ")))
# print(list_1) # почему сделали отдельно, т.к. мы должны работать с одним набором слов, а не с разными 
# index_find(input(),list_1) 




def spisok(count, word='abc'):
    my_list = []
    for i in range(count):
        temp = sample(word, k=3)
        my_list.append("".join(temp))
    return my_list


def index_find(word_2, list_2):
    if word_2 in list_2 and list_2.count(word_2) > 1:
        index_1 = list_2.index(word_2)
        print(list_2.index(word_2, index_1+1))
    else:
        print(-1)


list_1 = spisok(int(input()))
print(list_1)
index_find(input(), list_1)
# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import choice
# если в первом и втором файле одинаковое кол-во многочленов, то мы берём построчно 
# в первой строке всё кроме "=0", потом прибавляем из второго файла весь многочлен, 
# потомучто там уже есть "=0" и всё это прибавляем и отправляем в файл  
def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
        open(name_2, "r", encodid ="utf-8") as my_f_2: # вот так мы открываем 2 файла через запятую, \ нужен для того, чтобы не записывать код в длинную строку
        first = my_f_1.readlines() # метод считывает всю информацию в виде списка строк, 
        # и тут не нужно дополнительных циклов, тут всё и так считается
        second = my_f_2.readlines ()

        if len(first) == len(second): # если длины этих списков совпадают, то мы заходим внутрь и работаем 
            with open ("sum_poly. txt", "a", encoding="utf-8") as my_f_3: # важно что только после проверки на равенство длин создаём третий файл
                for i, v in enumerate(first):
                    my_f_3.write(f"{v[:-5]} + {second[i]}") # -5 - это мы убираем 5 элементов с конца (учитывая что вконце строчки стоят невидимые \n\r - переходы на новую строчку)
        else:
            print ("The contents of the files do not match!")

# poly_sum(input ("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
poly_sum("poly.txt", "poly_2.txt")


# Сложный вариант:

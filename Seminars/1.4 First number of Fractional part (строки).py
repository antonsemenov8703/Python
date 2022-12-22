#4. Показать первую цифру дробной части числа.
#  6,856 -> 8\

# a = 6.856
# a = a * 10
# print (a)
# a = int(a)
# print (a)
# print (a % 10)



# a = 11.823
# st = str(a)
# print(st.find('.'))
# d = st.find('.') # номер элемента с точкой
# print(st[d+1]) # запрос вывода следующего элемента, после которого обнаружена '.' 



# a = 11.823
# print(str(a)[str(a).find('.')+1]) # работа со строками 



# А можно сделать функцию для поиска любого элента после запятой или до запятой


def Number_after_decimal_point():
    a = input('Введите дробное число:  ')
    number = int(input('Введите какой элемент после запятой нужно вывести: '))
    print(str(a)[str(a).find('.')+number])

Number_after_decimal_point()




# def check_first_num():
#     number = float(input("Введите число: "))
#     new_num = int(number*10%10)
#     print(new_num)

# check_first_num()

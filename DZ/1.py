# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите номер дня недели: '))
print('Да' if 5 < number <= 7 else 'Нет')

# другой вариант:

# number = int(input('Введите номер дня недели: '))
# if 0 < number < 6: 
#     print ('Нет, это будний день')
# elif 5 < number < 8:
#     print ('Да, это выходной!')
# else: 
#     print ('В неделе 7 дней')






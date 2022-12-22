# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

number = int(input("Введите число: "))
number_list = []
number_sum = 0 
for i in range(number):
    number_list.append(round((1+1/(i+1))**(i+1),3))
    number_sum = number_sum + number_list[i]
    print(round(number_sum, 3))

print(number_list)
print(number_sum)


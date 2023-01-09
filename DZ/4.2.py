# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]


   
def simple_num_devisors(num):
    if num > 0 : 
        lst =[]

        for i in range (2,num):
            for k in range (2,num+1):
                if not num % k:
                    lst.append(k)
                    num = int(num/k)
                    break
        return lst
    else: print("Вы ввели некорректное число!")
    
print (simple_num_devisors(int(input("Введите число: "))))


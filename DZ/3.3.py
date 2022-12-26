# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

number = int(input("Введите десятичное число: "))

def decimal_to_binary(num_10):
    num_2 = []
    while num_10:
        num_2.append(num_10%2)
        num_10 //=2
    num_2.reverse()
    return num_2
    
print(decimal_to_binary(number))

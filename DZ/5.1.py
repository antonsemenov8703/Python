# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, 
# list comprehension

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect


# Первая функция делает набор из слов | count и подстроку из которой будет собираться "абв"
# sample возвращает список букв и их нужно будет join-ить а потом append | 
# Не используем choices, т.к. он даст повторяющиеся буквы, которые мы никогда не убирём

# Вторая функция перебирает  - не игнорирует "абв" что-то там join-ится тоже....

from random import sample

count = int(input("Enter number of words: "))

def word_list (count:int, word:str ='абв'):
    lst = []

    for i in range(count):
        temp = sample(word, k=len(word))  # sample возвращает список символов, по этому 
        lst.append("".join(temp)) # "".join сделает так, что символы встанут вплотную(join приводит list к str )
    return " ".join(lst) # тут повторно list приводим к str 


def del_word(string_1,word:str=' абв'):
    print(string_1.replace(word, ""))


string_0 = word_list(count)
print(string_0)
del_word(string_0)



# с разбора на семинаре
# from random import sample
# def list_rand_words (count: int, alp: str = 'абв'):
#     words_list = []
#     for i in range (count):
#         letters = sample (alp, k=3)
#         words_list.append("".join(letters))
#     return " ".join(words_list) 


# #def list_rand_words(count: int, alp: str = 'абв'):
# #   return " " join("' join (sample (alp, 3)) for - in range (count))


# def simple_sentence (words: str) -> str:
#     #return " ".join (words.replace("абв", "").split()) 
#     return " ".join(i for i in words.split() if i != "абв")


# all_list = list_rand_words (int (input ("Number of words: ")))
# print(all_list)
# print (simple_sentence (all_list))
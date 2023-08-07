# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
import random

def InputRandomArray():
    length = int(input("Введите длину массива: "))
    list = []
    for _ in range(length):
        list.append(random.randint(0, 200))
    return list

def RangeArray(list):
    min = int(input("Введите минимальное число диапазона: "))
    max = int(input("Введите максимальное число диапазона: "))
    result_list = []
    for n in range(len(list)):
        if min < list[n] and max > list[n]:
            result_list.append(n)
    print(list)
    return result_list

list = InputRandomArray()
print(RangeArray(list)) 
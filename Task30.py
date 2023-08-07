# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def MathDifference(length, first_elem, difference):
    list = [first_elem]
    i = 2
    for n in range(length):
        list.append(first_elem + (i - 1) * difference)
        i += 1
        print(f"{n + 1} число арифметической прогрессии: {list[n]}")
    return list


length = int(input("Введите длину массива: "))
first_elem = int(input("Введите первый элемент массива: "))
difference = int(input("Введите разность арифметической прогрессии: "))

MathDifference(length, first_elem, difference)
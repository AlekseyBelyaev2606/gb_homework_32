#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#
# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)
from pprint import pprint

tempList = input("Введите значение списка через пробел")
array = [int(i) for i in tempList.split()]
print(array)


minElement = int(input("Введите min"))
maxElement = int(input("Введите max"))
tempArray = {}

for i in range(0, len(array)):
    if array[i] > minElement and array[i] < maxElement:
        tempArray[i] = array[i]

pprint(tempArray)
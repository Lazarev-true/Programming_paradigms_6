# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве

def binary_search(arr, number):
    left = 0
    right = len(arr) - 1
    while left <= right:
        midst = (left + right) // 2
        if arr[midst] == number:
            return midst
        elif arr[midst] < number:
            left = midst + 1
        else:
            right = midst - 1
    return -1

arr = [int(x) for x in input('Введите массив целых чисел через пробел: ').split()]

print(f'Массив: {arr}')
number = int(input('Введите целое число: '))
result = binary_search(arr, number)

if result == -1:
    print('Элемент не найден (-1)')
else:
    print(f'Индекс: {result}')

# Task 1
'''Последовательностью Фибоначчи называется последовательность чисел 
a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 13
Задание необходимо решать через рекурсию'''

'''def fib(n):
    if n in (1, 2):
        return 1
    return fib(n-1) + fib(n-2)

n = int(input('Введите число n: '))
print(fib(n))'''


# Task 2
'''Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

'''
import time
import random

def max_to_min1(arr):
    set_arr = set(arr)
    min_arr = min(set_arr)
    max_arr = max(set_arr)
    return [min_arr if num == max_arr else num for num in arr]


def max_to_min2(arr):
    min_arr = arr[0]
    max_arr = arr[0]
    max_index = [0]
    for i in range(1, len(arr)):
        if arr[i] > max_arr:
            max_arr = arr[i]
            max_index = [i]
        elif arr[i] == max_arr:
            max_index.append(i)
        if arr[i] < min_arr:
            min_arr = arr[i]
    for i in max_index:
        arr[i] = min_arr


n = int(input('Введите количество оценок: '))
nums1 = [random.randint(1, 5) for num in range(n)]
nums2 = nums1.copy()


start1 = time.time()
max_to_min1(nums1)
end1 = time.time()
time1 = end1 - start1


start2 = time.time()
max_to_min2(nums2)
end2 = time.time()

print(time1)
print(end2 - start2)
'''

# Task 3
'''Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input:    2 -> 3 4
Output: 4 3'''

'''def revers_nums(count_nums, res = ''):
    if count_nums == 0:
        return res
    else:
        res = input('Введите число: ') + ' ' + res
        return revers_nums(count_nums - 1, res)

nums = int(input('Введите количество чисел '))
print(revers_nums(nums))'''

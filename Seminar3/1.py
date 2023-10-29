from random import randint
n = int(input('Введите количество чисел: '))
arr = []
for i in range(n):
    arr.append(randint(-100,100))
print(arr)
print(f'В массиве {len(set(arr))} уникальных чисел')
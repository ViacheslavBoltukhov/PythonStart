from random import randint
n = int(input('Введите количество чисел: '))
arr = []
count = 0
for i in range(n):
    arr.append(randint(-100,100))
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        #print(f'{arr[i]} > {arr[i - 1]}')
        count += 1
print(arr)
print(count)
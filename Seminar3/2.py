from random import randint
k = int(input('Введите коэффициент сдвига: '))
n = int(input('Введите количество чисел в массиве: '))
arr = []
for i in range(n):
    arr.append(randint(-100,100))
print(arr)
k = k % len(arr)
print(arr[-k : ] + arr[ : -k])

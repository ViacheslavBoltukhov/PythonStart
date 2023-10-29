'''Задача №9.
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while

Input: 5

Output: 120 '''
# Вариант1
n = int(input())
res_while = 1
i = 2
print('res_while')
while i <= n:
    res_while *= i
    i += 1
print(res_while)
# Вариант2
print('res_for')
res_for = 1
for i in range(2, n + 1):
    res_for *= i
print(res_for)
# 1.4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input("Введите целое положительное число "))
maxi = num % 10
while num >= 1:
    num = num // 10
    if num % 10 > maxi:
        maxi = num % 10
    elif num > 9:
        pass
print("Максимальное цифра в числе ", maxi)

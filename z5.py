n = int(input("Введите натуральное число: "))

a = 0
for i in range(1, n + 1):
    if n % i == 0:
        a += i
b = a

print("Сумма делителей числа {}: {}".format(n, b))

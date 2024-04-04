n = int(input("Введите количество элементов: "))
sum = 1.0
a = 1.0

for i in range(1, n):
    a *= -0.5
    sum += a
    print("{}: {}".format(i+1, a))

print("Сумма: {}".format(sum))
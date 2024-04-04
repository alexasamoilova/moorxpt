a = int(input("Введите высоту треугольника: "))

b = 0
for i in range(a):
    for j in range(i + 1):
        b += 1
        print(b, end=" ")
    print()

min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))
step = float(input("Введите шаг: "))
while min <= max:
    y = -0.5 * min + min
    print("x: {}, y: {}".format(min, y))
    min += step
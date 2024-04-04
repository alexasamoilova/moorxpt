number = int(input("Введите целое число (не меньше 2): "))
if number < 2:
    print("Число должно быть не меньше 2")
else:
    a = 2
    while number % a != 0:
        a += 1
    a
    print("Наименьший натуральный делитель: {}".format(a))

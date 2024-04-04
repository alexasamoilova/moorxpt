a = 10
day_7 = a

for day in range(2, 11):
    a *= 1.1
    print("Пробег лыжника за {} день: {} км".format(day, round(a, 2)))
    if day <= 7:
        day_7 += a

print("Суммарный путь за первые 7 дней тренировок: {} км".format(round(day_7, 2)))

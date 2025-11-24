spb_price = 50_000
msc_price = 80_000
ekb_price = 40_000

print("Приветствую в системе 'Помощь туриста'")
print("Доступны следующие города для расчёта стоимости билетов: spb, msc, ekb")
print("-----------------------------------")
city = input("Введите город, в который хотите поехать: ")
count = int(input("Введите количество туристов: "))

total = 0

if city == "spb":
    total = spb_price * count + spb_price * count / 2
elif city == "msc":
    total = msc_price * count + msc_price * count / 2
elif city == "ekb":
    total = ekb_price * count + ekb_price * count / 2
else:
    print("Введен город, которого нет!")
    exit()

print("Итоговый бюджет: " + str(total))
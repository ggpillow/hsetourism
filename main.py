spb_price = 50_000
msc_price = 80_000
ekb_price = 40_000

city = input("Введите город, в который хотите поехать: ")
parents_count = int(input("Введите количество туристов: "))
kids_count = int(input("Введите количество детей: "))

total = 0

if city == "spb":
    total = spb_price * parents_count + spb_price * kids_count / 2
elif city == "msc":
    total = msc_price * parents_count + msc_price * kids_count / 2
elif city == "ekb":
    total = ekb_price * parents_count + ekb_price * kids_count / 2
else:
    print("Введен город, которого нет!")
    exit()

print("Итоговый бюджет: " + str(total))
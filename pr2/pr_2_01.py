a = int(input("Введіть число: "))

count = 0
tot = 0

for i in range(1, a + 1):
    if i % 3 == 0 or i % 5 == 0:
        count += 1
        tot += i

print("Кількість", count)
print("Сума", tot)

if count > 0:
    avr = tot / count
    print("Середнє", avr)
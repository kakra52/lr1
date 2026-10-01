N = int(input("Введіть N: "))

if N == 0:
    count = 1
    total = 0
    max_digit = 0
    min_digit = 0
else:
    number = N
    count = 0
    total = 0
    max_digit = 0
    min_digit = 9

    while number > 0:
        digit = number % 10

        count += 1
        total += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        number //= 10

print("Кількість цифр:", count)
print("Сума цифр:", total)
print("Найбільша цифра:", max_digit)
print("Найменша цифра:", min_digit)
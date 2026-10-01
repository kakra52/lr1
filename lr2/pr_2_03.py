N = int(input("Введіть N: "))

for number in range(1, N + 1):
    temp = number
    valid = True

    while temp > 0:
        digit = temp % 10

        if digit != 0 and number % digit != 0:
            valid = False
            break

        temp //= 10

    if valid:
        print(number, end=" ")
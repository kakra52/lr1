def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def main():
    n = int(input("N = "))
    print("Просте число:", "так" if is_prime(n) else "ні")
    print("Дільники:", divisors(n))
    print("Сума цифр:", digit_sum(n))


main()
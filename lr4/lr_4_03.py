products = {
    "milk": 48,
    "bread": 32,
    "tea": 75
}

products["coffee"] = 120
products["bread"] = 35

name = input("Введіть назву товару: ")

price = products.get(name)

if price is not None:
    print(name, "—", price, "грн")
else:
    print("Товар не знайдено")

min_price = float(input("Мінімальна ціна: "))
max_price = float(input("Максимальна ціна: "))

print("Товари у заданому діапазоні:")

for name, price in products.items():
    if min_price <= price <= max_price:
        print(name, "—", price, "грн")
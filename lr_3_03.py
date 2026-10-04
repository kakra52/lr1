text1 = input("Введіть перший рядок: ")
text2 = input("Введіть другий рядок: ")

normal1 = "".join(text1.lower().split())
normal2 = "".join(text2.lower().split())

print("Нормалізований перший рядок:", normal1)
print("Нормалізований другий рядок:", normal2)

if sorted(normal1) == sorted(normal2):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")
text = input("Введіть текст: ")

letters = 0
digits = 0
spaces = 0
vowels = 0


vowel_letters = "аеєиіїоуюя"

for symbol in text:
    if symbol.isalpha():
        letters += 1

    if symbol.isdigit():
        digits += 1

    if symbol.isspace():
        spaces += 1

    if symbol.lower() in vowel_letters:
        vowels += 1

words = text.split()

print("Символів:", len(text))
print("Літер:", letters)
print("Цифр:", digits)
print("Пробілів:", spaces)
print("Голосних:", vowels)
print("Слів:", len(words))
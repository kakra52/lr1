sentence = input("Введіть речення: ")

words = sentence.split()

if len(words) > 0:
    max_length = len(words[0])
    min_length = len(words[0])

    for word in words:
        if len(word) > max_length:
            max_length = len(word)

        if len(word) < min_length:
            min_length = len(word)

    longest = []
    shortest = []

    for word in words:
        if len(word) == max_length and word not in longest:
            longest.append(word)

        if len(word) == min_length and word not in shortest:
            shortest.append(word)

    unique_words = set()

    for word in words:
        unique_words.add(word.lower())

    print("Найдовші:", ", ".join(longest))
    print("Найкоротші:", ", ".join(shortest))
    print("Унікальних слів:", len(unique_words))

    old_word = input("Введіть слово для заміни: ")
    new_word = input("Введіть нове слово: ")

    new_words = []

    for word in words:
        if word.lower() == old_word.lower():
            new_words.append(new_word)
        else:
            new_words.append(word)

    result = " ".join(new_words)

    print("Після заміни:", result)

else:
    print("Речення порожнє.")
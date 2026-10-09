def check_length(password):
    return len(password) >= 8


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_upper(password):
    return any(char.isupper() for char in password)


def has_lower(password):
    return any(char.islower() for char in password)


def has_special(password):
    return any(not char.isalnum() for char in password)


def validate_password(password):
    errors = []

    if not check_length(password):
        errors.append("менше 8 символів")
    if not has_digit(password):
        errors.append("немає цифри")
    if not has_upper(password):
        errors.append("немає великої літери")
    if not has_lower(password):
        errors.append("немає малої літери")
    if not has_special(password):
        errors.append("немає спеціального символу")

    return len(errors) == 0, errors


def main():
    password = input("Password: ")
    valid, errors = validate_password(password)

    if valid:
        print("Пароль надійний")
    else:
        print("Пароль не відповідає вимогам.")
        for error in errors:
            print("Не виконано:", error)


main()
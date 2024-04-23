import re
import sys

def length(password):
    """Перевіряє довжину пароля."""
    return len(password) >= 8

def digit(password):
    """Перевіряє, чи містить пароль принаймні одну цифру."""
    return bool(re.search(r'\d', password))

def uppercase(password):
    """Перевіряє, чи містить пароль принаймні одну велику літеру."""
    return bool(re.search(r'[A-Z]', password))

def lowercase(password):
    """Перевіряє, чи містить пароль принаймні одну малу літеру."""
    return bool(re.search(r'[a-z]', password))

def special_char(password):
    """Перевіряє, чи містить пароль принаймні один спеціальний символ."""
    return bool(re.search(r'[!@#$%^&*()_=+-]', password))

def validate_password(password):
    """Перевіряє, чи відповідає пароль усім критеріям."""
    if not length(password):
        print("Пароль не відповідає критеріям: пароль повинен містити принаймні 8 символів.", file=sys.stderr)
        return False
    if not digit(password):
        print("Пароль не відповідає критеріям: пароль повинен містити принаймні одну цифру.", file=sys.stderr)
        return False
    if not uppercase(password):
        print("Пароль не відповідає критеріям: пароль повинен містити принаймні одну велику літеру.", file=sys.stderr)
        return False
    if not lowercase(password):
        print("Пароль не відповідає критеріям: пароль повинен містити принаймні одну малу літеру.", file=sys.stderr)
        return False
    if not special_char(password):
        print("Пароль не відповідає критеріям: пароль повинен містити принаймні один спеціальний символ.", file=sys.stderr)
        return False
    return True


def enter_password():
    return input("Введіть пароль: ")

if __name__ == "__main__":
    import sys
    password = enter_password()
    if validate_password(password):
        print("Пароль відповідає критеріям.")
        sys.exit(0)
    else:
        sys.exit(1)

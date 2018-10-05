import re


def print_password_strength(strength):
    print('Сложность Вашего пароля:', strength, 'из 10')


def get_password():
    user_password = input('Введите пароль: ')
    return user_password


def get_password_strength(password_for_check):
    strength = 0

    if len(password_for_check) >= 12:
        strength += 3
    elif len(password_for_check) >= 8:
        strength += 2

    if re.search(r'[A-ZА-Я]', password_for_check):
        strength += 2

    if re.search(r'[a-zа-я]', password_for_check):
        strength += 1

    if re.search(r'[0-9]', password_for_check):
        strength += 2

    if re.search(r'[\W_]', password_for_check):
        strength += 2

    return strength


if __name__ == '__main__':
    password = get_password()
    password_strength = get_password_strength(password)
    print_password_strength(password_strength)

import re


def print_password_strength(strength):
    print('Сложность Вашего пароля:', strength, 'из 10')


def get_password():
    user_password = input('Введите пароль: ')
    return user_password


def check_for_upper_case(password_for_check):
    if re.search(r'[A-ZА-Я]', password_for_check):
        return 2
    else:
        return 0


def check_for_lower_case(password_for_check):
    if re.search(r'[a-zа-я]', password_for_check):
        return 1
    else:
        return 0


def check_for_special_character(password_for_check):
    if re.search(r'[\W_]', password_for_check):
        return 2
    else:
        return 0


def check_length(password_for_check):
    if len(password_for_check) >= 12:
        return 3
    elif len(password_for_check) >= 8:
        return 2
    else:
        return 0


if __name__ == '__main__':
    password = get_password()
    password_strength = 0
    password_strength += check_length(password)
    password_strength += check_for_lower_case(password)
    password_strength += check_for_upper_case(password)
    password_strength += check_for_special_character(password)
    print_password_strength(password_strength)

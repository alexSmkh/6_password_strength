import re
import getpass


def print_password_strength(strength):
    print('Сложность Вашего пароля:', strength, 'из 10')


def get_password():
    user_password = getpass.getpass('Введите пароль: ')
    return user_password


def check_for_upper_case(password_for_check):
    return bool(re.search(r'[A-ZА-Я]', password_for_check))


def check_for_lower_case(password_for_check):
    return bool(re.search(r'[a-zа-я]', password_for_check))


def check_for_special_character(password_for_check):
    return bool(re.search(r'[\W_]', password_for_check))


def check_for_digit(password_for_check):
    return bool(re.search(r'[\d]', password_for_check))


def check_length(password_for_check):
    recommended_length_password = 8
    return bool(len(password_for_check) >= recommended_length_password)


if __name__ == '__main__':
    password = get_password()
    password_strength = 0
    multiplier_to_estimate_password_complexity = 2
    password_strength = sum([
        check_length(password),
        check_for_lower_case(password),
        check_for_upper_case(password),
        check_for_special_character(password),
        check_for_digit(password)]
    )
    print_password_strength(password_strength * multiplier_to_estimate_password_complexity)

import re
import getpass
import json


def load_from_json(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def check_symbols(password):
    score = sum([int(bool(re.search(r'[0-9]', password)) * 2),
                 int(bool(re.search(r'[a-z]', password)) * 2),
                 int(bool(re.search(r'[A-Z]', password)) * 2),
                 int(bool(re.search(r'[!@#$%&*()~{}]', password)) * 4)])
    return score


def check_blacklist(password):
    black_list = load_from_json('blacklist.json')
    for word in black_list:
        if password == word:
            return -10
    return 0


def check_length(password):
    length_scores = len(password) / 2.0
    if length_scores > 10:
        length_scores = 10
    return length_scores


def get_password_strength(password):
    total_scores = 0
    total_scores += check_blacklist(password)
    total_scores += check_length(password)
    total_scores += check_symbols(password)
    if total_scores < 0:
        total_scores = 0
    return int(total_scores / 2.0)


if __name__ == '__main__':
    password = getpass.getpass('Пароль: ')
    print(get_password_strength(password))

import re
import getpass
import string
import os


def load_blacklist(filepath):
    with open(filepath, 'r') as file_handler:
        read_data = file_handler.read()
    blacklist = re.findall(r"[\w']+", read_data)
    return blacklist


def check_symbols(password):
    score = sum([int(bool(re.search(r'[0-9]', password)) * 2),
                 int(bool(re.search(r'[a-z]', password)) * 2),
                 int(bool(re.search(r'[A-Z]', password)) * 2),
                 ((any(char for char in password
                       if char in string.punctuation)) * 4)])
    return score


def check_blacklist(password, blacklist):
    for word in blacklist:
        if password == word:
            return -10
    return 0


def check_length(password):
    length_scores = len(password) / 2.0
    max_length_scores = 10
    if length_scores > max_length_scores:
        length_scores = max_length_scores
    return length_scores


def get_password_strength(password, blacklist):
    total_scores = 0
    total_scores += check_blacklist(password, blacklist)
    total_scores += check_length(password)
    total_scores += check_symbols(password)
    if total_scores < 0:
        total_scores = 0
    return int(total_scores / 2.0)


if __name__ == '__main__':
    if os.path.isfile('blacklist.txt'):
        password = getpass.getpass('Пароль: ')
        blacklist = load_blacklist('blacklist.txt')
        print(get_password_strength(password, blacklist))
    else:
        print('Error: No such file in directory')

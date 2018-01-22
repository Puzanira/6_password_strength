import re


black_list = ['qwerty',
              'asdfg',
              '12345',
              'password',
              '00000',
              '98765']

def check_symbols(password):
    score = 0
    if re.search(r'[0-9]', password):
        score += 2
    if re.search(r'[a-z]', password):
        score += 2
    if re.search(r'[A-Z]', password):
        score += 2
    if re.search(r'[!@#$%&*()~{}]', password):
        score += 4
    return score


def check_blacklist(password):
    score = 0
    for word in black_list:
        if password.find(word) != -1:
            score -= 5
    return score


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
    password = input('Пароль: ')
    print(get_password_strength(password))

import re


black_list = ['qwerty',
              'asdfg',
              '12345',
              'password',
              '00000',
              '98765']

def get_password_strength(password):
    scores = 0
    length_scores = len(password) / 2.0
    if length_scores > 10:
        scores += 10
    else:
        scores += length_scores
    if re.search(r'[0-9]', password):
        scores += 2
    if re.search(r'[a-z]', password):
        scores += 2
    if re.search(r'[A-Z]', password):
        scores += 2
    if re.search(r'[!@#$%&*()~{}]', password):
        scores += 4
    for word in black_list:
        if password.find(word) != -1:
            scores -= 5
    if scores < 0:
        scores = 0
    return int(scores / 2.0)


if __name__ == '__main__':
    password = input('Пароль: ')
    print(get_password_strength(password))

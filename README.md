# Password Strength Calculator

Estimates your passoword, gives it a score from 0 to 10

## Blacklist checkout:

In file **"blacklist.json"** (in this repo) there is a list of 
[500 most common passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/500-worst-passwords.txt)

This program checks if your password is in that list. If so, it will return **"0"**. 

## Scores

* **+2** if your password contains _lowcase letters_
* **+2** if your password contains _uppercase letters_
* **+2** if your password contains _digits_
* **+4** if your password contains _special symbols (like !%@)_
* **+lengh scores** - your password length divided by 2 (max 10)

You can get maximum **20** scores. Then program divides it by 2 and prints out.

## How to use:

**Launch:**
```bash
$ python password_strength.py
$ Password: <type_your_password>
$ 8
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

import random
import string
import os

def generate_random_txt(file_path, length=1000):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_text = ''.join(random.choice(characters) for _ in range(length))
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(random_text)

def count_characters(file_path):
    upper_case = 0
    lower_case = 0
    digits = 0
    others = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            if char.isupper():
                upper_case += 1
            elif char.islower():
                lower_case += 1
            elif char.isdigit():
                digits += 1
            else:
                others += 1

    print(f"Upper case letters: {upper_case}")
    print(f"Lower case letters: {lower_case}")
    print(f"Digits: {digits}")
    print(f"Other characters: {others}")

if __name__ == "__main__":
    test_file_path = r'./实验/实验二/test.txt'
    generate_random_txt(test_file_path)
    count_characters(test_file_path)
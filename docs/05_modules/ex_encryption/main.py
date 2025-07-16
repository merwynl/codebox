import random
import string


def encryption_program():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()

    random.shuffle(key)

    # print(f"chars: {chars}")
    # print(f"key: {key}")

    # ENCRYPT
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Original Msg: {plain_text}")
    print(f"Encrypted Msg: {cipher_text}")

    # DECRYPT
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted Msg: {cipher_text}")
    print(f"Original Msg: {plain_text}")
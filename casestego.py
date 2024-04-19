import string
import sys

ASCII = """
   ██████      ██      ████████ ████████  ████████ ██████████ ████████   ████████    ███████  
  ██░░░░██    ████    ██░░░░░░ ░██░░░░░  ██░░░░░░ ░░░░░██░░░ ░██░░░░░   ██░░░░░░██  ██░░░░░██ 
 ██    ░░    ██░░██  ░██       ░██      ░██           ░██    ░██       ██      ░░  ██     ░░██
░██         ██  ░░██ ░█████████░███████ ░█████████    ░██    ░███████ ░██         ░██      ░██
░██        ██████████░░░░░░░░██░██░░░░  ░░░░░░░░██    ░██    ░██░░░░  ░██    █████░██      ░██
░░██    ██░██░░░░░░██       ░██░██             ░██    ░██    ░██      ░░██  ░░░░██░░██     ██ 
 ░░██████ ░██     ░██ ████████ ░████████ ████████     ░██    ░████████ ░░████████  ░░███████  
  ░░░░░░  ░░      ░░ ░░░░░░░░  ░░░░░░░░ ░░░░░░░░      ░░     ░░░░░░░░   ░░░░░░░░    ░░░░░░░   """


def encode(plaintext: str, secret_text: str) -> str:
    bin_string = ""
    for letter in secret_text:
        bin_string += bin(ord(letter))[2:].zfill(8)
    print(f"Bin secret: {bin_string}")

    count_letters = 0
    for letter in plaintext:
        if letter in string.ascii_letters:
            count_letters += 1

    if count_letters < len(bin_string):
        return "Less letters"

    encoded_text = ""
    bin_i = 0
    for letter in plaintext:
        current_letter = letter
        if letter in string.ascii_letters and bin_i < len(bin_string):
            if bin_string[bin_i] == "1":
                current_letter = letter.upper()
            else:
                current_letter = letter.lower()
            bin_i += 1
        encoded_text += current_letter

    return encoded_text


def decode(encoded_text: str) -> str:
    bin_string = ""
    for letter in encoded_text:
        if letter in string.ascii_letters:
            if letter.isupper():
                bin_string += "1"
            else:
                bin_string += "0"

    print(f"Bin secret: {bin_string}")
    secret_text = ""
    for i in range(0, len(bin_string), 8):
        secret_text += chr(int(bin_string[i : i + 8], 2))

    return secret_text


print(ASCII)
mode = input("\nEnter mode ([E]ncode/[D]ecode): ")

if mode in ["E", "e"]:
    plaintext = input("Enter plaintext: ")
    secret_text = input("Enter secret text: ")
    encoded_text = encode(plaintext, secret_text)
    print(f"Encoded text: {encoded_text}")
elif mode in ["D", "d"]:
    encoded_text = input("Enter encoded text: ")
    secret_text = decode(encoded_text)
    print(f"Secret text: {secret_text}")
else:
    print("Invalid mode")
    sys.exit(1)

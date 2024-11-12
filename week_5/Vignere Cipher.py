keyword = "random"

def encrypt_text(letter, shift):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if letter.isalpha():
            base = abc.index(letter)
            base = (base + shift) % 26
            secret_letter = abc[base]
        else:
         secret_letter = letter
        return secret_letter


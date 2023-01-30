def letter_to_number(letter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    # Find the number corresponding to the given letter.
    # In this case a = 0, b = 1, c = 2, ..., z= 25.
    number = letters.index(letter)
    return number


def number_to_letter(index):
    letters = "abcdefghijklmnopqrstuvwxyz"
    # Find the letter corresponding to the given number.
    # In this case 0 = a, 1 = b, 2 = c, ..., 25 = z.
    return letters[index]


def shift(letter, value):
    n = letter_to_number(letter)
    return number_to_letter((n + value) % 26)


def rot(string, value):
    ciphertext = ""
    for letter in string:
        try:
            ciphertext += shift(letter, value)
        except:
            ciphertext += letter
    return ciphertext


def decode(string, value):
    plaintext = ""
    for letter in string:
        try:
            plaintext += shift(letter, -value)
        except:
            plaintext += letter
    return plaintext


'''plainTextInput = input("Plain text: ").lower()
cipherText1 = rot(plainTextInput, 13)
print("rot13:", cipherText1)
cipherText2 = rot(plainTextInput, 2)
print("rot2:", cipherText2)

cipherTextInput = input("Cipher text: ").lower()
decodeValue = int(input("Shift: "))
decodedText1 = decode(cipherTextInput, decodeValue)
print("decoded:", decodedText1)'''

file = open("plaintext.txt", "r")
plainString = ""
for line in file:
    plainString += line
print(plainString)
cipherString = rot(plainString, 13)
print(cipherString)
file.close()

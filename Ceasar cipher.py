from datetime import date

today = date.today()
switch = today.strftime("%d")
move0 = switch[0]
move1 = switch[1]
move = int(move0) + int(move1)


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char == " ":
            result += "_"
        elif char == ".":
            result += "."
        elif char == ",":
            result += ","
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(message, da):
    trans = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters2 = "abcdefghijklmnopqrstuvwxyz"
    print(len(message))
    for i in range(len(message)):
        char = message[i]
        if char in letters:
            num = letters.find(char)
            num -= da
            if num < 0:
                num += len(letters)
            trans += letters[num]
        elif char in letters2:
            num2 = letters2.find(char)
            num2 -= da
            if num2 < 0:
                num2 += len(letters2)
            trans += letters2[num2]
        else:
            trans += char
    return trans


check = input("Would you like to encrypt or decrypt a message? ")
check = check.lower()
if check[0] == "e":
    t = input("What is the text you would like encoded: ")
    td = encrypt(t, move)
    print(td)
elif check[0] == "d":
    d = input("Please enter the message you want decrypted: ")
    print(decrypt(d, move))

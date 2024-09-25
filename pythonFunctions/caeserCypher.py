alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, and 'decode' to decrypt: ")
text = input("Type your message: ")
shift = int(input("Type the shift number: "))
length = len(alphabet_list)


def encodeFunction(enteredText, shiftNumber):
    actualText = ""
    for letter in enteredText:
        position = alphabet_list.index(letter)
        newPosition = position+shiftNumber
        newLetter = alphabet_list[newPosition]
        actualText += newLetter
    print(f"New letter is: {actualText} ")

def decodeFunction(cipherText, shiftNumber):
    PlainText = ""
    for letter in cipherText:
        position = alphabet_list.index(letter)
        newPosition = position-shiftNumber
        newLetter = alphabet_list[newPosition]
        PlainText += newLetter
    print(f"The decrypted message is: {PlainText}")

if direction == "encode":
    encodeFunction(enteredText= text, shiftNumber= shift)
elif direction == "decode":
    decodeFunction(cipherText= text, shiftNumber= shift)
import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

symbols = [
    '!', '@', '#', '$', '%',  '&', '*', '-', '_', '=', '+', '?', '~', 
]

noOfAlphabets = int(input("how many letters would you want in password"))
noOfNumbers = int(input("How many mumbers would you want"))
noOfSymbols = int(input("How many symbols would you want"))

password = []
for charcter in range(1,noOfAlphabets+1): 
   password +=random.choice(letters)

for character in range(1, noOfNumbers+1):
   password += random.choice(numbers)

for character in range(1, noOfSymbols+1):
   password += random.choice(symbols)
random.shuffle(password)
passw = ""
for character in password:
   passw +=character

print(f"your password is {passw}")   
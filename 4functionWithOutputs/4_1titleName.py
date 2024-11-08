def formatName(fName, lName):
    first = fName.title()
    last = lName.title()
    return f"{first} {last}"


fName = input("Enter your first name: ")
lName= input("Enter the last name: ")
Name = formatName(fName, lName)
print(Name)
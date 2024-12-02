#first way
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
#file.close()
from certifi import contents

#second way, close option not required

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

    #but this way it wont be able to write, to write wee need to add mode

with open("my_file.txt", mode="w") as f:
    f.write("this is the new one")  #but this will clear previous contents
# not to clear, we use mode = "a"

with open('my_file.txt', mode="a") as f:
    f.write("\nok! this is appended")

with open("az.txt", mode="a")as n:
    n.write("this")
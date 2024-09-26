import math

def paintCansRequired(w, h, c):
    req = math.ceil((w * h)/c)
    print(f"total cans required are {req} ")


height = int(input("Enter the height of wall: "))
width = int(input("Enter the width of wall: "))
coverage = 5

paintCansRequired(width, height, coverage)

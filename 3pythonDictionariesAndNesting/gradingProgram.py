marks = {
    "A":98,
    "B":64,
    "C":83,
    "D":81,
    "E":72,
    "F":84,
    "G":78,
}

grades = {}

for key in marks:
    if marks[key] >90:
        grades[key] = "Outstanding"
    elif marks[key]>80:
        grades[key] = "Excellent"
    elif marks[key]>70:
        grades[key] = "Very good"
    elif marks[key]>60:
        grades[key] = "Good"
    else:
        grades[key] = "Fail"
print(grades)   
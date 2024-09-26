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
    if marks[key]<90 and marks[key]>80:
        grades[key] = "Excellent"
    if  marks[key]<80 and marks[key]>70:
        grades[key] = "Very good"
    if marks[key]<70 and marks[key]>60:
        grades[key] = "Good"
print(grades)   
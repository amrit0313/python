import pandas

students_dict = {
    "students": ["alex", "amrit", "aana", "suhana", "brayno", "ruby", "sibra"],
    "score":[68, 75, 27, 72, 76, 29, 75]
}
students_dataframe = pandas.DataFrame(students_dict)
print(students_dataframe)

#loop through a dataframe
# for(key, value) in students_dataframe.items():
#     print(key) #only students and score is printed
#     print(value) #only the data inside keys are printed
#not that useful


#we can loop through each of the row of dataframes rather than columns
for (index, row) in students_dataframe.iterrows():
    # print(row)
    if row.students == "amrit":
        print(row.score)

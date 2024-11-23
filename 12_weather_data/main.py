# with open("002 weather-data.csv") as f:
#     contents = f.readlines()
#     print(contents)

# import csv
#
# with open("002 weather-data.csv") as file:
#     contents = csv.reader(file)
#     temp = []
#     for row in contents:
#         if row[1] !="temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas
data = pandas.read_csv('002 weather-data.csv')
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
data_list = data["temp"].to_list()
# # avg = sum(data_list)/len(data_list)
# avg = data["temp"].mean()
# print(avg)
# maximum = data["temp"].max()
# print(maximum)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
# print(monday.condition)
monday_temp = int(monday.temp) * 9/5 +32
print(monday_temp)

students = {
    'st':['am', 'as', 'ad'],
    'score':[10, 20, 30]
}

dataf = pandas.DataFrame(students)
print(dataf)
dataf.to_csv("datafiles.csv")
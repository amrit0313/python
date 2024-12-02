#
# # first basic
# try:
#     file = open("the_file.txt")
#     dict_name = {"key":"value"}
#     print(dict_name["key"])
# except FileNotFoundError:  # we have filenotfound here because if we won't do it won't display key error, which happened in dictionary, which isn't the exception that we want to address
#     file = open("the_file.txt", "w")
#     file.write("a big thing")
#
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exists")
#
# else: # if no error occur this will run
#     content = file.read()
#     print(content)
#
# finally:
#     # raise KeyError("this is done when key doesn't match")
#     file.close()
#     print("file was closed")
#
#
#
#
#
#
# #raising own exception
# height = float(input("Enter you height in m: "))
# weight = int(input("Enter your weight in kg: "))
#
#
# if height>3:
#     raise ValueError("Human height shouldn't be over 3m")
#
# bmi = weight/height ** 2
# print(bmi)
#
#
#
#
#
#
#
# # working with index error
# fruits = ["apple", "pear", "banana"]
#
# def make_pie(index):
#     try:
#         fruit_pie = fruits[index]
#     except IndexError:
#         print("fruit_pie")
#     else:
#         print(fruit_pie+ "pie")
#
# make_pie(3)
#
#
#



#working with key errors
facebook_posts = [
    {"likes":21, "comments": 6},
    {"likes": 5, "comments": 1},
    {"likes": 26, "comments": 9},
    {"shares": 12, "comments": 5},
    {"likes": 23, "comments": 7}
]

total_likes = 0

for posts in facebook_posts:
    try:
        total_likes = total_likes+ posts["likes"]
    except KeyError:
        pass

print(total_likes)

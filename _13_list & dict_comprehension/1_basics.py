import random

from pygments.lexer import words

#list comprehension

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers) ## will print [2, 3, 4]


name = "Amrit"
new_name = [letters for letters in name]
print(new_name) # this will convert string to list with each letter as a item


new = [n*2 for n in range(1,5)]
print(new) #will print [2, 4, 6, 8]



#conditional list comprehension
#new_item for item in list if condition

names = ['alex', 'amrit', "aana", "suhana", "braynol", "ruby", "sibra"]
short_names = [name for name in names if len(name) <5]
print(short_names)
long_names = [name.upper() for name in names if len(name) >5]
print(long_names)
#dictionaries comprehension
students = {name:random.randint(10, 100) for name in names} #dictionary comprehension
print(students)
passed_students = {student:score for (student,score) in students.items() if score >60 }
print(passed_students)





## some exercises
num_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 65]
squares = [n**2 for n in num_list]
print(squares)
even_numbers = [n for n in num_list if n%2 == 0]
print(even_numbers)


# more on dictionary comprehension

sentence = "how much is the air speed of something that falls down in absence of air"
sentence_list = sentence.split()
sentence_dict = {words:len(words) for words in sentence_list }
print(sentence_dict)

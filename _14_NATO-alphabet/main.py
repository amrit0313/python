import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dictionary)

user_input = input("enter your name: ").upper()
code_list = [data_dictionary[letter] for letter in user_input]
print(code_list)
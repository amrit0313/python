import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetics():
    user_input = input("enter your name: ").upper()
    try:
        code_list = [data_dictionary[letter] for letter in user_input]
    except KeyError:
        print("Please enter a valid name, with alphabet letters only")
        generate_phonetics()

    else:
        print(code_list)

generate_phonetics()
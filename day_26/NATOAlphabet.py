import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

user_input = input("Enter a word: ").upper()
lists_letters = [character for character in user_input]
create_code = [phonetic_dict[letter] for letter in lists_letters if letter in phonetic_dict]
print(lists_letters)
print(create_code)

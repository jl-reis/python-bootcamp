import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creates dictionary from df with the Letter as index
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


not_a_word = True
while not_a_word:
    try:
        user_word = input("Type a word: ").upper()
        user_list = [nato_dict[letter] for letter in user_word]
        not_a_word = False
    except KeyError as key_error:
        print("Sorry, only letters, please")
    else:
        print(user_list)

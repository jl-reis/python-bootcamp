# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as model:
    with open("./Input/Names/invited_names.txt") as names_file:
        all_names = names_file.readlines()
        letter = model.read()
        for _ in range(0, len(all_names)):
            all_names[_] = all_names[_].strip("\n")
        for name in all_names:
            user_letter = letter.replace("[name]", name)
            with open(f"letter_to_{name}", "w") as final_user_letter:
                final_user_letter.write(user_letter)

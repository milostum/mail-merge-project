PLACEHOLDER = "[name]"


with open("Input/Letters/starting_letter.docx") as letter_file:
    my_text = letter_file.read()

with open("./Input/Names/invited_names.txt", mode="r") as file_with_names:
    names = file_with_names.readlines()

for name in names:
    stripped_name = name.strip("\n")
    letter_text = my_text.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as letter:
        letter.write(letter_text)

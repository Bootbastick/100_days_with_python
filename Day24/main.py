# 4.Making 3 previous steps repeat with other names
with open("Input/names.txt", mode="r") as f:
    all_names = f.read()
num_of_names = all_names.count("\n")
for i in range(num_of_names):
    # 1.Take one name from names.txt
    with open("Input/names.txt") as file:
        name = file.readlines()
        name = name[i]
    file_directory = f"Output/letter_for_{name}.txt"
    file_directory = file_directory.replace("\n", "")

    # 2.Make text for with persons name in it instead of [name]
    with open("Input/example_letter.txt", mode="r") as text:
        mail = text.read()
    mail_for_name = mail.replace("[name]", name)
    mail_for_name = mail_for_name.replace("\n", "", 1)

    # 3.Make file in Output folder with name and text
    with open(file_directory, mode="w") as letter:
        letter.write(mail_for_name)

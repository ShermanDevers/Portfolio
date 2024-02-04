import string
import random


class Gen:
    def __init__(self, pass_length):
        self.passwd = "".join(
            random.choice(string.digits + string.ascii_letters + string.punctuation)
            for x in range(pass_length)
        )


def write():
    with open("possible_passwords.txt", "a") as writing:
        writing.write(f"{passwd.passwd}\n")


possible_pass = int(input("How many passwords do you want to create?: "))
ran_or_fixed = str(input("Do you want the length to be random or chosen?: "))

if ran_or_fixed in ["random", "Random"]:
    for x in range(possible_pass):
        pass_length = random.randint(10, 20)
        passwd = Gen(pass_length)
        write()

if ran_or_fixed in ["chosen", "Chosen"]:
    pass_length = int(input("How long do you want them do be?: "))
    for x in range(possible_pass):
        chara = Gen(pass_length)
        write()

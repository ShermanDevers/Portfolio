mapping = {
    "A": "Z",
    "B": "Y",
    "C": "X",
    "D": "W",
    "E": "V",
    "F": "U",
    "G": "T",
    "H": "S",
    "I": "R",
    "J": "Q",
    "K": "P",
    "L": "O",
    "M": "N",
    "N": "M",
    "O": "L",
    "P": "K",
    "Q": "J",
    "R": "I",
    "S": "H",
    "T": "G",
    "U": "F",
    "V": "E",
    "W": "D",
    "X": "C",
    "Y": "B",
    "Z": "A",
    "1": "0",
    "2": "9",
    "3": "8",
    "4": "7",
    "5": "6",
    "6": "5",
    "7": "4",
    "8": "3",
    "9": "2",
    "0": "1",
    " ": " ",
    "<": "<",
    "-": "-",
    "'": "",
    '"': "",
    "\n": "\n",
}


def cipher(original):
    message = ""
    for char in original:
        char = str(char)
        char = char.upper()
        new_char = mapping[char]
        message += new_char
    return message

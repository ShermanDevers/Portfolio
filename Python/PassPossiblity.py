import string
import random

poschara = int(input("How many possible characters for each space: "))
amountofspaces = int(input("How many spaces: "))
print(f"{poschara ** amountofspaces:,}")

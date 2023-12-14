import string

special = string.punctuation
minimum_length = 12
numbers = string.digits
passed = "✓"
failed = "✗"


passwd_test = input("Enter a password to test its strength: ")

if len(passwd_test) >= minimum_length:
    length_test = passed
else:
    length_test = failed

if any(char in special for char in passwd_test):
    special_test = passed
else:
    special_test = failed

if any(char in numbers for char in passwd_test):
    number_test = passed
else:
    number_test = failed

print("Test Results")
print(f"Length: {length_test}")
print(f"Special Characters: {special_test}")
print(f"Numbers: {number_test}")

import os

files = []
not_allowed = ["lines_of_code.py","go.mod","requirements.txt","README.md"]
file_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(file_dir)

def count_together():
    linecount = 0
    for file in files:
        with open(file,"r") as linecount_file:
            content = linecount_file.readlines()
            for line in content:
                if line != "\n":
                    linecount += 1
    print(f"Together all files have {linecount} lines")

def count_individual():
    for filename in files:
        with open(filename,"r") as linecount_file:
            linecount = 0
            content = linecount_file.readlines()
            for line in content:
                if line != "\n":
                    linecount += 1
            print(f"{filename} has {linecount} lines of code.")

def main():
    for file in os.listdir():
        if os.path.isfile(file) and file not in not_allowed:
            files.append(file)

    together_or_individual = input("Count individual files or together: ")

    if together_or_individual == "individual":
        count_individual()
    else:
        count_together()



if __name__ == "__main__":
    main()
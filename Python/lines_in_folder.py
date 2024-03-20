import os


def list_files(not_allowed):
    return [
        file
        for file in os.listdir()
        if os.path.isfile(file) and file not in not_allowed
    ]


def count_together(folders, file_dir, not_allowed):
    folders.append(file_dir)
    total_line_count = 0

    for folder in folders:
        if folder == file_dir:
            print(f"{folder.split("/")[-1].title()}")
        else:
            print(f"{folder}")

        os.chdir(folder)
        files = list_files(not_allowed)

        for file in files:
            linecount = 0
            with open(file, "r") as file_r:
                linecount += sum(1 for line in file_r if line != "\n")

            print(f"{'==>':>10}{file}: {linecount}")

            total_line_count += linecount
        os.chdir("..")

    print(f"{total_line_count} lines total in all present folders")


def main():
    folders = [
        folder
        for folder in os.listdir()
        if os.path.isdir(folder) and not folder.startswith(".")
    ]
    not_allowed = ["lines_of_code.py", "go.mod", "requirements.txt", "README.md"]
    file_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_dir)
    count_together(folders, file_dir, not_allowed)


if __name__ == "__main__":
    main()

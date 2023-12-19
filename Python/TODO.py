import sys


def edit():
    with open("Tasks.txt", "r") as tasks:
        contents = tasks.read()

    for task in contents.split("\n"):
        if task == "":
            continue

        print(f"> {task}")

    add_or_remove = input("Would you like to add(A) or remove(R) a task?: ")
    match add_or_remove:
        case "A":
            task_num = int(input("Amount of tasks you want to add?: "))
            for i in range(task_num):
                action_to_do = input("What do you need to do?: ")
                with open("Tasks.txt", "a") as tasks:
                    tasks.write(f"{action_to_do}\n")

        case "R":
            task_num = int(input("Amount of tasks you want to remove?: "))
            for i in range(task_num):
                action_to_do = input("What have you completed: ")
                with open("Tasks.txt", "r") as tasks:
                    contents = tasks.read()
                with open("Tasks.txt", "w") as tasks:
                    for task in contents.split("\n"):
                        if task == action_to_do:
                            continue
                        tasks.write(f"{task}\n")


def clear():
    with open("Tasks.txt", "w") as tasks:
        tasks.write("")


def main():
    while True:
        with open("Tasks.txt", "x") as tasks:
            tasks.write("")

        with open("Tasks.txt", "r") as tasks:
            contents = tasks.read()

        for task in contents.split("\n"):
            if task == "":
                continue
            print(f"> {task}")

        action = input("Edit(E), Clear(C) or Exit(X): ")
        match action:
            case "E":
                edit()
            case "C":
                clear()
            case "X":
                sys.exit()


if __name__ == "__main__":
    main()

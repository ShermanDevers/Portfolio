import random
import sys

print("Welcome to the Casino!")


def next_item(item, possible_items: list):
    return possible_items[(possible_items.index(item) + 1) % len(possible_items)]


def prev_item(item, possible_items: list):
    return possible_items[(possible_items.index(item) - 1) % len(possible_items)]


def deposit(money):
    depo = int(input("How much would you like to deposit?: "))
    money += depo
    print(f"Money: {money}")
    return money


def slot_machine(chosen_item, amount):
    matches = 0
    print(f"Betting amount {amount}")

    possible_items = ["Cherry", "Diamond", "Gold"]
    item_1 = random.choice(possible_items)
    item_2 = random.choice(possible_items)
    item_3 = random.choice(possible_items)

    item_1_prev = prev_item(item_1, possible_items)
    item_1_next = next_item(item_1, possible_items)

    item_2_next = next_item(item_2, possible_items)
    item_2_prev = prev_item(item_2, possible_items)

    item_3_prev = prev_item(item_3, possible_items)
    item_3_next = next_item(item_3, possible_items)

    print("\n")
    print(f"{item_1_prev}  {item_2_prev}  {item_3_prev}")
    print(f"{item_1}  {item_2}  {item_3}")

    print(f"{item_1_next}  {item_2_next}  {item_3_next}")
    print("\n")

    if item_1 == chosen_item:
        matches += 1
    if item_2 == chosen_item:
        matches += 1
    if item_3 == chosen_item:
        matches += 1

    if matches > 1:
        amount *= 2
        print(f"You won {amount}!")
    else:
        print(f"You lost {amount}!")
        amount = 0
    return amount


def bet_choices(money):
    bet_item = input("What item would you like to bet on? (Diamond, Gold, Cherry): ")

    while True:
        betting_amount = int(
            input(
                "Betting amount (you get double if you get 2 or more of the chosen item): "
            )
        )
        if betting_amount > money:
            print("Can't bet more than you have!")
            continue
        else:
            break

    money_won = slot_machine(bet_item, betting_amount)
    money = money + money_won
    return money


def main():
    money = 0

    while True:
        if money > 0:
            continue_q = input("Continue(c) or Quit(q): ")
            match continue_q:
                case "c":
                    bet_choices(money)
                case "q":
                    print(f"You left with {money}")
                    sys.exit()
                case "":
                    print("Not an option!")
                    continue

        depo_or_quit = input("Deposit(d) or Quit(q)?: ")

        match depo_or_quit:
            case "d":
                money = deposit(money)
            case "q":
                print(f"You left with {money}")
                sys.exit()
            case "":
                print("Not an option")
                continue
        money = bet_choices(money)


if __name__ == "__main__":
    main()

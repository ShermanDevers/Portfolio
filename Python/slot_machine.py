import random
import sys

print("Welcome to the Casino!")


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
    
    item_1_prev = possible_items[(possible_items.index(item_1) - 1) % len(possible_items)]
    item_1_next = possible_items[(possible_items.index(item_1) + 1) % len(possible_items)]

    item_2_next = possible_items[(possible_items.index(item_2) + 1) % len(possible_items)]
    item_2_prev = possible_items[(possible_items.index(item_2) - 1) % len(possible_items)]

    item_3_next = possible_items[(possible_items.index(item_3) + 1) % len(possible_items)]
    item_3_prev = possible_items[(possible_items.index(item_3) - 1) % len(possible_items)]


    print("\n")
    print(
        f"{item_1_prev}  {item_2_prev}  {item_3_prev}"
    )
    print(f"{item_1}  {item_2}  {item_3}")

    print(
        f"{item_1_next}  {item_2_next}  {item_3_next}"
    )
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


def main():
    money = 0

    while True:
        depo_or_quit = input("Deposit(d) or Quit(q)?: ")
        match depo_or_quit:
            case "d":
                money = deposit(money)
            case "q":
                print(f"You left with {money}")
                sys.exit()

        bet_item = input(
            "What item would you like to bet on? (Diamond, Gold, Cherry): "
        )
        betting_amount = int(
            input(
                "Betting amount (you get double if you get 2 or more of the chosen item): "
            )
        )
        money = slot_machine(bet_item, betting_amount)


if __name__ == "__main__":
    main()

import random
import time

player = {"Health": 100, "Defense": 0}
opponent = {"Health": 100, "Defense": 0}


opp_moves = ["Fireball", "Fire wall"]
opp_move_damage = {"Fireball": 40, "Fire wall": 30}
moves = {"Offense": {"Water Bullet": 40}, "Defense": {"Water Prism": 30}}


def players_turn(opponent_health, defense, opponent_defense):
    print("\nPlayer's turn")
    print(f"Available moves")
    print(f"Offense: {moves['Offense']}")
    print(f"Defense: {moves['Defense']}")
    move_type = input("What category is your move under?: ")

    if move_type == "defense":
        move_to_use = input("What move do you want to use?: ")
        category_moveset = moves[move_type.title()]
        defense += category_moveset[move_to_use.title()]

    if move_type == "offense":
        move_to_use = input("What move do you want to use?: ")
        category_moveset = moves[move_type.title()]
        damage_from_player = category_moveset[move_to_use.title()]
        opponent_health -= damage_from_player - opponent_defense
    print(f"Opponents Health: {opponent_health}")
    print("End of player's turn")
    return "Bot"


def bots_turn(player_health, defense, opponent_defense):
    print("Bots Turn")
    time.sleep(0.5)
    random_move = random.sample(opp_moves, 1)
    chosen_move = "".join(random_move)
    print(f"Bot chose {chosen_move}")
    if chosen_move == "Fire wall":
        opponent_defense += opp_move_damage[chosen_move]
    time.sleep(0.5)
    print(f"Your Health: {player_health}")
    time.sleep(0.5)
    print("End of Bots turn")

    if chosen_move == "Fireball":
        time.sleep(0.5)
        damage_from_opponent = opp_move_damage[chosen_move]
        print(f"You took {damage_from_opponent} damage")
        if damage_from_opponent < 0:
            damage_from_opponent = 0
        player_health -= damage_from_opponent - defense
    return "Player"


confirm = input("Do you want to play a game?: ")
if confirm in ["Y", "y", "yes"]:
    first_turn = input("Who goes first player or bot?: ")
    if first_turn in ["player"]:
        next_turn = players_turn(
            opponent["Health"], player["Defense"], opponent["Defense"]
        )

    if first_turn in ["bot"]:
        bots_turn(player["Health"], player["Defense"], opponent["Defense"])


def main():
    while player["Health"] > 0 or opponent["Health"] > 0:
        if next_turn == "Player":
            next_turn = players_turn(
                opponent["Health"], player["Defense"], opponent["Defense"]
            )
        if next_turn == "Bot":
            next_turn = bots_turn(
                player["Health"], player["Defense"], opponent["Defense"]
            )


if __name__ == "__main__":
    main()

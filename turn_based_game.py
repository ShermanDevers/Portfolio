import random
import time


health = 100
opp_health = 100

defense = 0
opp_defense = 0

opp_moves = ["Fireball", "Fire wall"]
opp_move_damage = {"Fireball": 40, "Fire wall": 30}
moves = {"Offense": {"Water Bullet": 40}, "Defense": {"Water Prism": 30}}


def Players_turn(opponent_health, defense, opponent_defense):
    print("\nPlayer's turn")
    print(f"Available moves")
    print(f"Offense: {moves['Offense']}")
    print(f"Defense: {moves['Defense']}")
    move_type = input("What category is your move under?: ")

    if move_type == "defense":
        move_to_use = input("What move do you want to use?: ")
        category_moveset = moves[move_type.title()]
        defense += category_moveset[move_to_use]

    if move_type == "offense":
        move_to_use = input("What move do you want to use?: ")
        category_moveset = moves[move_type.title()]
        damage_from_player = category_moveset[move_to_use]
        opponent_health -= damage_from_player - opponent_defense
    print(f"Opponents Health: {opponent_health}")
    print("End of player's turn")
    return "Bot"


def Bots_turn(player_health, defense, opponent_defense):
    print("Bots Turn")
    time.sleep(0.5)
    random_move = random.sample(opp_moves, 1)
    chosen_move = "".join(random_move)
    print(f"Bot chose {chosen_move}")
    if chosen_move == "Fire wall":
        opp_defense
    time.sleep(0.5)
    damage_from_opponent = opp_move_damage[chosen_move]
    print(f"You took {damage_from_opponent} damage")
    player_health -= damage_from_opponent - defense
    time.sleep(0.5)
    print(f"Your Health {player_health}")
    time.sleep(0.5)
    print("End of Bots turn")
    return "Player"


confirm = input("Do you want to play a game?: ")
if confirm in ["Y", "y", "yes"]:
    first_turn = input("Who goes first player or bot?: ")
    if first_turn in ["player"]:
        next_turn = Players_turn(opp_health, defense, opp_defense)

    if first_turn in ["bot"]:
        Bots_turn(health, opp_defense)


while health > 0 or opp_health > 0:
    if next_turn == "Player":
        next_turn = Players_turn(opp_health, defense, opp_defense)
    if next_turn == "Bot":
        next_turn = Bots_turn(health, defense, opp_defense)

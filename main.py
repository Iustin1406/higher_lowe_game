from dictionary import celebrities_dict
from random import randrange

max_score = len(celebrities_dict)
compared = [False] * max_score


def new_celebrity():
    """Returns a new celebrity from celebrity_list who has never been selected"""
    position = randrange(max_score)
    while compared[position] == True:
        position = randrange(max_score)
    return position


still_playing = True
score = 0
first_celebrity = randrange(max_score)
compared[first_celebrity] = True

while still_playing == True and score < max_score:
    second_celebrity = new_celebrity()
    compared[second_celebrity] = True
    print(f"ROUND {score+1}\n")
    print(celebrities_dict[first_celebrity]["name"])
    print(celebrities_dict[first_celebrity]["description"])
    print(celebrities_dict[first_celebrity]["country"])
    print("\nVS\n")
    print(celebrities_dict[second_celebrity]["name"])
    print(celebrities_dict[second_celebrity]["description"])
    print(celebrities_dict[second_celebrity]["country"])

    choice = input("\nPress 'H' if the first one is higher or 'L' if it's lower: ")
    if (choice == 'H' and celebrities_dict[first_celebrity]["follower_count"] > celebrities_dict[second_celebrity][
        "follower_count"]) \
            or (
            choice == 'L' and celebrities_dict[first_celebrity]["follower_count"] < celebrities_dict[second_celebrity]["follower_count"]):
        score += 1
        print('\n')
    else:
        still_playing = False
        print(f"You lost! Your score is: {score}")

    first_celebrity = second_celebrity

if score == max_score:
    print("Congratulations! You won the game")

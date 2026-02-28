import random
def get_choices():
    player_choice=input("Enter your choice[Rock/Paper/Scissors]")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"you choose {player}, computer choose {computer}")
    if player==computer:
        return "It's a Tie"
    elif player=="rock" and computer=="scissors":
        return "Player wins"
    elif player=="scissors" and computer=="rock":
        return "Computer wins"
    elif player=="paper" and computer=="rock":
        return "Player wins"
    elif player=="rock" and computer=="paper":
        return "Computer win"
    elif player=="paper" and computer=="scissors":
        return "Computer win"
    elif player=="scissors" and computer=="paper":
        return "Player win"
    
choices=get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
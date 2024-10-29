import random
print("Your options are:\n1. Rock\n2. Paper\n3. Scissors")
options= ("Rock","Paper","Scissors")

playing= True

while playing:
    player= None
    computer= random.choice(options)

    while (player not in options):
        player= input("Enter your choice: ")

    print(f"Player: {player}")
    print(f"Cpmputer: {computer}")

    if player==computer:
        print("Its a tie")

    elif player== "rock" and computer== "scissors":
        print("You win :)")

    elif player== "paper" and computer== "rock":
        print("You win :)")

    elif player== "scissors" and computer== "rock":
        print("You win :)")

    else:
        print("You loose :(")
    
    play_again= input("Do you want to play again? (y/n): ").lower()
    if play_again=="n":
        playing=False

print("Okay see you soon :)")
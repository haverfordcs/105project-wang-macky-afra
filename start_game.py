import random

# Go over rules
# Decide who starts through a game of rock, paper, scissor
# add letters
# lowercase RPS , add space after input


def Start():
    print("Welcome to Battleship! Do you know the rules of Battleship?")
    display_rules = False
    while display_rules == False:
        rules = input("Input 'Yes' or 'No': ")
        if rules == 'Yes' or rules == 'yes':
            display_rules = True
            print("Ok! Start by placing your ships on your board - ")
            #return True

        elif rules == 'No' or rules == 'no':
            display_rules = True
            print('''
            The objective of the game is to sink all of your opponent's ships
            Here are the rules of Battleship:
            Each player places 5 ships somewhere on their board either vertically or horizontally
            Ships may not overlap
            The five ships are:
            Aircraft Carrier (5 spaces), Battleship (4 spaces), Destroyer (3 spaces), Submarine (3 spaces), Patrol Boat (2 spaces)
            Players take turn guessing their opponent's ship placements by calling out coordinates
            The boards will display a hit, a miss, or a sunken ship
            As soon as all of one player's ships have been sunk, the game ends!
            
            Legend: (+) = Miss | (X) = Hit | (O) = Friendly Ship | (V) = Sunken Ship
            
            Start by placing your ships on your board -
            ''')
            #return True
        else:
            print("Error: That is not a valid entry")


# Whoever wins starts the game
def RockPaperScissors():
    print("Play rock, paper, scissors to decide who shoots first!")
    # True = player wins
    # False = AI wins
    player = False
    while player == False:
        AI = random.randint(1, 3)
        # print("AI has chosen!")
        if AI == 1:
            AI_choice = "rock"
        elif AI == 2:
            AI_choice = "paper"
        else:
            AI_choice = "scissors"
        player = input("Rock, Paper, or Scissors? ").lower()
        if player == AI_choice:
            print("Tie!")

        elif player == "rock":
            if AI_choice == "paper":
                print("AI chose paper. Paper covers rock.")
                print("You lose! AI shoots first")
                x = input("Press enter to continue")
                return False
            else:
                print("AI chose scissors. Rock smashes scissors.")
                print("You win! You shoot first")
                x = input("Press enter to continue")
                return True

        elif player == "paper":
            if AI_choice == "scissors":
                print("AI chose scissors. Scissors cut paper.")
                print("You lose! AI shoots first")
                x = input("Press enter to continue")
                return False
            else:
                print("AI chose rock. Paper covers rock.")
                print("You win! You shoot first")
                x = input("Press enter to continue")
                return True

        elif player == "scissors":
            if AI_choice == "rock":
                print("AI chose rock. Rock smashes scissors.")
                print("You lose! AI shoots first")
                x = input("Press enter to continue")
                return False
            else:
                print("AI chose paper. Scissors cut paper.")
                print("You win! You shoot first")
                x = input("Press enter to continue")
                return True

        else:
            print("That's not a valid play. Check your spelling!")

        player = False

if __name__ == "__main__":
    #Start()
    x = 1
    while x:
        RockPaperScissors()

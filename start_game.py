import random

#Go over rules
#Decide who starts through a game of rock, paper, scissor
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


#Whoever wins starts the game
def RockPaperScissors():
        print("Play rock, paper, scissors to decide who shoots first!")

        #True = player wins
        #False = AI wins
        player = False
        while player == False:
            AI = random.randint(1, 3)
            AI_choice = AI
            if AI == 1:
                AI_choice = "rock"
            elif AI == 2:
                AI_choice = "paper"
            elif AI == 3:
                AI_choice = "scissors"
            player = input("Rock, Paper, or Scissors? ").lower()
            if player == AI_choice:
                print("Tie!")

            elif player == "rock":
                if AI_choice == "paper":
                    print("AI chose:", AI_choice, ".", AI_choice, "covers", player)
                    print("You lose! AI shoots first")
                    return False
                else:
                    print("AI chose:", AI_choice,".", player, "smashes", AI_choice)
                    print("You win! You shoot first")
                    return True

            elif player == "paper":
                if AI_choice == "scissors":
                    print("AI chose:", AI_choice, ".", AI_choice, "cuts", player)
                    print("You lose! AI shoots first")
                    return False
                else:
                    print("AI chose:", AI_choice,".", player, "covers", AI_choice)
                    print("You win! You shoot first")
                    return True

            elif player == "scissors":
                if AI_choice == "rock":
                    print("AI chose:", AI_choice, ".", AI_choice, "covers", player)
                    print("You lose! AI shoots first")
                    return False
                else:
                    print("AI chose:", AI_choice,".", player, "cuts", AI_choice)
                    print("You win! You shoot first")
                    return True

            else:
                print("That's not a valid play. Check your spelling!")

            player = False


#Start()
#RockPaperScissors()

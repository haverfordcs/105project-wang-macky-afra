import random

#Go over rules
#Decide who starts through a game of rock, paper, scissor


def Start():
    print("Welcome to Battleship! + Do you know the rules of Battleship?")
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
            The opponent's board will return with values to indicate "hit" or "miss"
            When all of the coordinates that a ship occupies have been hit, the ship will be sunk
            As soon as all of one player's ships have been sunk, the game ends!
            
            Start by placing your ships on your board -
            ''')
            #return True
        else:
            print("Error: That is not a valid entry")


#Whoever wins starts the game
def RockPaperScissors():

        AI = random.randint(1,3)
        AI_choice = AI
        if AI == 1:
            AI_choice = "Rock"
        elif AI == 2:
            AI_choice = "Paper"
        elif AI == 3:
            AI_choice = "Scissors"



        player = False
        while player == False:
            player = input("Rock, Paper, or Scissors?")
            if player == AI_choice:
                print("Tie!")
                break
            elif player == "Rock":
                if AI_choice == "Paper":
                    print("You lose!", AI_choice, "covers", player)
                else:
                    print("You win!", player, "smashes", AI_choice)
                break
            elif player == "Paper":
                if AI_choice == "Scissors":
                    print("You lose!", AI_choice, "cuts", player)
                else:
                    print("You win!", player, "covers", AI_choice)
                break
            elif player == "Scissors":
                if AI_choice == "Rock":
                    print("You lose...", AI_choice, "smashes", player)
                else:
                    print("You win!", player, "cuts", AI_choice)
                break
            else:
                print("That's not a valid play. Check your spelling!")

            player = False


Start()

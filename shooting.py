# File for player shooting and AI shooting. Does NOT include prompting player input and sink detection
import random
# Temporary matrices for testing
# playerBoard = ([['O','O','O','O','O','O','O','O',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],['O','O','O','O','O','O','O','O',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],['O','O','O','O','O','O','O','O',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],['O','O','O','O','O','O','O','O',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],['O','O','O','O','O','O','O','O',' ',' ']])
# enemyBoard = ([['I','I',' ',' ','V',' ',' ',' ',' ',' '],[' ',' ',' ',' ','V',' ',' ',' ','X',' '],[' ',' ','X',' ','V',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ','X',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ','X',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
def printBoard(player):
    print("---------------------------------------------")
    print("                 Your Board                  ")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    print("|   | A | B | C | D | E | F | G | H | I | J |")
    for i in range(len(player)):
        row = str(i)
        print("|---|---|---|---|---|---|---|---|---|---|---|")
        print("| " + row + " | " + player[i][0] + " | " + player[i][1] + " | " + player[i][2] + " | " + player[i][3] + " | " + player[i][4] + " | " + player[i][5] + " | " + player[i][6] + " | " + player[i][7] + " | " +player[i][8] + " | " + player[i][9] + " |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")


def printBothBoards(player, opponent):
    print("-------------------------------------------------------------------------------------------------")
    print("                 Your Board                                          Enemy Board                 ")
    print("|---|---|---|---|---|---|---|---|---|---|---|       |---|---|---|---|---|---|---|---|---|---|---|")
    print("|   | A | B | C | D | E | F | G | H | I | J |       |   | A | B | C | D | E | F | G | H | I | J |")
    for i in range(len(player)):
        row = str(i)
        print("|---|---|---|---|---|---|---|---|---|---|---|       |---|---|---|---|---|---|---|---|---|---|---|")
        print("| "+row+" | "+player[i][0]+" | "+player[i][1]+" | "+player[i][2]+" | "+player[i][3]+" | "+player[i][4]+" | "+player[i][5]+" | "+player[i][6]+" | "+player[i][7]+" | "+player[i][8]+" | "+player[i][9]+" |       | "+row+" | "+opponent[i][0]+" | "+opponent[i][1]+" | "+opponent[i][2]+" | "+opponent[i][3]+" | "+opponent[i][4]+" | "+opponent[i][5]+" | "+opponent[i][6]+" | "+opponent[i][7]+" | "+opponent[i][8]+" | "+opponent[i][9]+" |")
    print("|---|---|---|---|---|---|---|---|---|---|---|       |---|---|---|---|---|---|---|---|---|---|---|")
    print("(+) = Miss | (X) = Hit | (O) = Friendly Ship | (V) = Sunken Ship |")

# Function that hides all 'I', which are hidden enemy ships that the viewer shouldn't see
def hideHidden(opponent):
    hidden = []
    for i in range(len(opponent)):
        hidden.append(opponent[i].copy())
    for i, x in enumerate(hidden):
        for j, a in enumerate(x):
            if 'I' in a:
                hidden[i][j] = a.replace('I', ' ')
    return hidden


def check_valid_coordinates(square):  # Checks if a given string input is a valid square in the form 'A1'.
    if len(square) == 2:
        row = square[1:]
        if row == "0" or row == "1" or row == "2" or row == "3" or row == "4" or row == "5" or row == "6" or row == "7" or row == "8" or row == "9":
            if square[:1] in "ABCDEFGHIJabcdefghij" and int(square[1:]) in range(0, 10):
                # print("{}{} is a valid set of coordinates. Checking validity of placement.".format(input[:1],input[1:]))
                valid = True
            else:
                print("{}{} is not a valid set of coordinates.".format(square[:1], square[1:]))
                valid = False
            return valid
        else:
            valid = False
            print("{}{} is not a valid set of coordinates.")
            return valid
    else:
        valid = False
        print("{}{} is not a valid set of coordinates.")
        return valid


def coordinate_converter(square):  # Takes A1 (as a string) and turns it into a tuple (0,0)
    column_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
    if check_valid_coordinates(square):
        coordinates = ((column_dict[square[:1]]), (int(square[1:])))
        # print(coordinates)
        return coordinates
    else:
        print("Tried to convert invalid coordinates")

def playerShot(playerBoard, enemyBoard):
    # Keeps firing if you target a tile you have already shot at before
    firing = 1
    while firing == 1:
        target = input("Coordinates: ")
        if check_valid_coordinates(target) == True:
            row = coordinate_converter(target)[1]
            column = coordinate_converter(target)[0]

            # Hit
            if enemyBoard[row][column] == "I":
                enemyBoard[row][column] = "X"
                printBothBoards(playerBoard, hideHidden(enemyBoard))
                print("You hit an enemy ship!")
                firing = 0

            # Miss
            elif enemyBoard[row][column] == " ":
                enemyBoard[row][column] = "+"
                printBothBoards(playerBoard, hideHidden(enemyBoard))
                print("You missed!")
                firing = 0

            # Already shot here - shoot again
            else:
                print("You have already shot at these coordinates. Try again.")
    x = input("Press enter to continue")


enemyShotHitTrackerPerShip = []
enemyShotPreviousHit = ()
enemyShotTargetAcquired = False
enemyShotDirection = random.randint(1,4)
#       1
#     4 + 2
#       3

def enemyShot(playerBoard, enemyBoard):
    global enemyShotTargetAcquired
    global enemyShotDirection
    global enemyShotHitTrackerPerShip
    global enemyShotPreviousHit
    firing = 1
    while firing == 1:
        # If a ship is currently targeted
        if enemyShotTargetAcquired == True:
            print("TARGET ACQUIRED")
            # Check if targeted ship is sunk
            if playerBoard[enemyShotPreviousHit[0]][enemyShotPreviousHit[1]] == "V":
                # Ship destroyed. No longer have target
                # Clears ship hit tracker
                enemyShotHitTrackerPerShip = []
                enemyShotTargetAcquired = False
                # Continuing Loop
                firing = 1

            # Check if targeted ship is not sunk
            if playerBoard[enemyShotPreviousHit[0]][enemyShotPreviousHit[1]] == "X":
                print("PREVIOUS SHOT WAS HIT")
                validDirection = False
                # Correcting direction of aim if aiming at border
                while validDirection == False:
                    # If aiming down at bottom border
                    if enemyShotDirection == 3 and enemyShotPreviousHit[1] == 9:
                        enemyShotDirection = 1
                        validDirection = True
                    # If aiming up at top border
                    if enemyShotDirection == 1 and enemyShotPreviousHit[1] == 0:
                        enemyShotDirection = 3
                        validDirection = True
                    # If aiming right at right border
                    if enemyShotDirection == 2 and enemyShotPreviousHit[0] == 9:
                        enemyShotDirection = 4
                        validDirection = True
                    # If aiming left at left border
                    if enemyShotDirection == 4 and enemyShotPreviousHit[0] == 0:
                        enemyShotDirection = 2
                        validDirection = True
                    else:
                    # Aimed direction is valid
                        validDirection = True
                print("DIRECTION IS VALID")
                # Shoots in direction
                # Shoot up
                if enemyShotDirection == 1:
                    row = enemyShotPreviousHit[0] - 1
                    column = enemyShotPreviousHit[1]
                # Shoot down
                if enemyShotDirection == 3:
                    row = enemyShotPreviousHit[0] + 1
                    column = enemyShotPreviousHit[1]
                # Shoot right
                if enemyShotDirection == 2:
                    row = enemyShotPreviousHit[0]
                    column = enemyShotPreviousHit[1] + 1
                # Shoot left
                if enemyShotDirection == 4:
                    row = enemyShotPreviousHit[0]
                    column = enemyShotPreviousHit[1] - 1

                # Hit
                if playerBoard[row][column] == "O":
                    playerBoard[row][column] = "X"
                    printBothBoards(playerBoard, hideHidden(enemyBoard))
                    print("VALID TARGET FOUND")
                    print("Enemy hit!")

                    enemyShotHitTrackerPerShip.append((row, column))
                    enemyShotPreviousHit = (row, column)
                    enemyShotTargetAcquired = True
                    # Ending Loop
                    firing = 0

                # Miss
                elif playerBoard[row][column] == " ":
                    playerBoard[row][column] = "+"
                    printBothBoards(playerBoard, hideHidden(enemyBoard))
                    print("Enemy miss!")
                    # If only one spot in ship has been hit so far
                    if len(enemyShotHitTrackerPerShip) == 1:
                        print(enemyShotDirection)
                        enemyShotDirection = random.randint(1,4)
                        print("ONLY ONE SPOT. DIRECTION RANDOMIZED")
                        print(enemyShotDirection)
                    # If multiple spots in ship have been hit so far
                    else:
                        print("MULTIPLE SPOTS. DIRECTION SWAPPED")
                        print(enemyShotDirection)
                        # Same column
                        if enemyShotHitTrackerPerShip[0][1] == enemyShotHitTrackerPerShip[1][1]:
                            # Flip up to down
                            if enemyShotDirection == 1:
                                enemyShotDirection = 3
                            # Flip down to up
                            if enemyShotDirection == 3:
                                enemyShotDirection = 1
                        # Same row
                        if enemyShotHitTrackerPerShip[0][0] == enemyShotHitTrackerPerShip[1][0]:
                            # Flip left to right
                            if enemyShotDirection == 4:
                                enemyShotDirection = 2
                            # Flip right to left
                            if enemyShotDirection == 2:
                                enemyShotDirection = 4
                        print(enemyShotDirection)
                        print(enemyShotPreviousHit)
                        enemyShotPreviousHit = enemyShotHitTrackerPerShip[0]
                        print(enemyShotPreviousHit)
                    # Ending Loop
                    firing = 0

                # Already shot here - shoot again
                else:
                    print(enemyShotDirection)
                    print("ENEMY SHOT HERE ALREADY. CHANGING DIRECTION")
                    # If only one spot in ship has been hit so far
                    if len(enemyShotHitTrackerPerShip) == 1:
                        print(enemyShotDirection)
                        enemyShotDirection = random.randint(1, 4)
                        print("ONLY ONE SPOT. DIRECTION RANDOMIZED")
                        print(enemyShotDirection)
                    # If multiple spots in ship have been hit so far
                    else:
                        print("MULTIPLE SPOTS. DIRECTION SWAPPED")
                        print(enemyShotDirection)
                        # Same column
                        if enemyShotHitTrackerPerShip[0][1] == enemyShotHitTrackerPerShip[1][1]:
                            # Flip up to down
                            if enemyShotDirection == 1:
                                enemyShotDirection = 3
                            # Flip down to up
                            if enemyShotDirection == 3:
                                enemyShotDirection = 1
                        # Same row
                        if enemyShotHitTrackerPerShip[0][0] == enemyShotHitTrackerPerShip[1][0]:
                            # Flip left to right
                            if enemyShotDirection == 4:
                                enemyShotDirection = 2
                            # Flip right to left
                            if enemyShotDirection == 2:
                                enemyShotDirection = 4
                        print(enemyShotDirection)

                        # Continuing Loop
                        firing = 1
        # If no ship is currently targeted
        if enemyShotTargetAcquired == False:
            row = random.randint(0, 9)
            column = random.randint(0, 9)

            # Hit
            if playerBoard[row][column] == "O":
                playerBoard[row][column] = "X"
                printBothBoards(playerBoard, hideHidden(enemyBoard))
                print("Enemy hit!")

                enemyShotHitTrackerPerShip.append((row, column))
                enemyShotPreviousHit = (row, column)
                enemyShotTargetAcquired = True
                # Ending Loop
                firing = 0
                break

            # Miss
            elif playerBoard[row][column] == " ":
                playerBoard[row][column] = "+"
                printBothBoards(playerBoard, hideHidden(enemyBoard))
                print("Enemy miss!")
                # Ending Loop
                firing = 0

            # Already shot here - shoot again
            else:
                # Continuing Loop
                firing = 1

# Need to check for sinks. Once all ships are sunk make gameActive = False

# PLACE SHIPS HERE
#
# gameActive = True
# printBothBoards(playerBoard, hideHidden(enemyBoard))
# while gameActive == True:
#     playerShot()
#     # INSERT check_sink HERE
#     enemyShot()
#     # INSERT check_sink HERE
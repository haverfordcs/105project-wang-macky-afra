# File for player shooting and AI shooting. Does NOT include prompting player input and sink detection
import random
# Temporary matrices for testing
playerBoard = ([['O','O','O','O','O',' ',' ',' ',' ',' '],[' ','I',' ',' ','O',' ',' ',' ',' ',' '],[' ',' ',' ',' ','O',' ',' ',' ',' ',' '],[' ',' ',' ',' ','O',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
enemyBoard = ([['I','I',' ',' ','V',' ',' ',' ',' ',' '],[' ',' ',' ',' ','V',' ',' ',' ','X',' '],[' ',' ','X',' ','V',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ','X',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ','X',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
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

def playerShot():

    # Keeps firing if you target a tile you have already shot at before
    firing = 1
    while firing == 1:
        target = input("Coordinates: ")
        if check_valid_coordinates(target) == True:
            row = coordinate_converter(target)[1]
            column = coordinate_converter(target)[0]

            # OLD CODE
            # # Checking for valid column input
            # validColumnInput = 0
            # while validColumnInput == 0:
            #     column = str(input("Column: "))
            #     if column == "A":
            #         column = 0
            #         validColumnInput = 1
            #     elif column == "B":
            #         column = 1
            #         validColumnInput = 1
            #     elif column == "C":
            #         column = 2
            #         validColumnInput = 1
            #     elif column == "D":
            #         column = 3
            #         validColumnInput = 1
            #     elif column == "E":
            #         column = 4
            #         validColumnInput = 1
            #     elif column == "F":
            #         column = 5
            #         validColumnInput = 1
            #     elif column == "G":
            #         column = 6
            #         validColumnInput = 1
            #     elif column == "H":
            #         column = 7
            #         validColumnInput = 1
            #     elif column == "I":
            #         column = 8
            #         validColumnInput = 1
            #     elif column == "J":
            #         column = 9
            #         validColumnInput = 1
            #     else:
            #         print("Input a valid column (A-J)")
            #
            # # Checking for valid row input
            # validRowInput = 0
            # while validRowInput == 0:
            #     row = input("Row: ")
            #     if str(row) != "0" and str(row) != "1" and str(row) != "2" and str(row) != "3" and str(row) != "4" and str(row) != "5" and str(row) != "6" and str(row) != "7" and str(row) != "8" and str(row) != "9":
            #         print("Input a valid row (0-9)")
            #     else:
            #         row = int(row)
            #         validRowInput = 1


            # Hit
            if enemyBoard[row][column] == "I":
                enemyBoard[row][column] = "X"
                printBothBoards(playerBoard, hideHidden(enemyBoard))
                print("Hit!")
                firing = 0

            # Miss
            elif enemyBoard[row][column] == " ":
                enemyBoard[row][column] = "+"
                printBothBoards(playerBoard, hideHidden(enemyBoard))
                print("Miss!")
                firing = 0

            # Already shot here - shoot again
            else:
                print("You have already shot at these coordinates")
    x = input("Press enter to continue")
enemyShotTracker = []
enemyShotPrevious = ()
def enemyShot(enemyShotTracker, enemyShotPrevious):
    firing = 1
    while firing == 1:
        row = random.randint(0,9)
        column = random.randint(0,9)

        # Hit
        if playerBoard[row][column] == "O":
            playerBoard[row][column] = "X"
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy hit!")
            enemyShotTracker.append((row,column))
            enemyShotPrevious = (row,column)
            print(enemyShotTracker)
            # Ending Loop
            firing = 0

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
    x = input("Press enter to continue")
# Need to check for sinks. Once all ships are sunk make gameActive = False
gameActive = True
printBothBoards(playerBoard, hideHidden(enemyBoard))
while gameActive == True:
    playerShot()
    printBothBoards(playerBoard, hideHidden(enemyBoard))
    enemyShot(enemyShotTracker,enemyShotPrevious)
    printBothBoards(playerBoard, hideHidden(enemyBoard))

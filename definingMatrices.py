# This file will create the blank matrices that will be manipulated throughout the game.
# Details:
# 10 x 10 playing board
# Numbered 0-9 down side
# Numbered A-J across top

# Values
# +     (Miss)
#       (Empty)
# O     (Friendly Ship)
# X     (Hit Enemy Ship
# V     (Sunken Enemy Ship)
# I     (Hidden Enemy Ship)


# How to reference the board
# board[i][j] where j = 0 refers to column A and j = 9 refers to column J
# board[i][j] where i = 0 refers to row 0 and i = 9 refers to row 9
# All data is stored as strings

# Board of the player
playerBoard = ([[' ','I',' ',' ',' ',' ',' ',' ',' ',' '],[' ','I',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
# Board of the enemy containing all data (hidden ships, misses, hit ships, etc)
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

# Function that hides all 'I', which are hidden enemy ships that the viewer shouldn't see
def hideHidden(opponent):
    hidden = opponent
    for i, x in enumerate(hidden):
        for j, a in enumerate(x):
            if 'I' in a:
                hidden[i][j] = a.replace('I', ' ')
    return hidden


if __name__ == "__main__":
    # For setting up ships
    printBoard(playerBoard)

    # What the board actually is
    printBothBoards(playerBoard, enemyBoard)

    # What the board looks like for the player
    printBothBoards(playerBoard, hideHidden(enemyBoard))
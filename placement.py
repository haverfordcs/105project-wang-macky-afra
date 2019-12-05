# This file governs ship placement for both the player and the AI. It will have to be imported to the game file in
# order for the game to be run.
playerBoard = ([[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
import definingMatrices as dM

def ship_placement_player(matrix):  # This function runs through the ship-placement sequence for the player. Call it
    # when you want the player to place their ships. It takes an empty matrix and lets the player fill it with ships.
    print(type(matrix))
    if not board_is_clear(matrix):  # if the board is empty
        print("Board is not clear!")
    else:
        ships_list = [('Aircraft Carrier', 5), ('Battleship', 4), ('Destroyer', 3), ('Submarine', 3), ('Patrol Boat', 2)]
        for ship in ships_list:
            print("You are placing your {}. It is {} squares long.".format(ship[0], ship[1]))  # Tell the player which ship they're placing and how long it is
            placed = False
            while not placed:  # This exists so that it'll keep trying every time you give it a bad placement.
                valid_orientation = False
                while not valid_orientation:  # This exists so that it'll keep trying every time you give it a bad orientation.
                    print("Would you like to place your ship vertically or horizontally?")  # ask player if they want it horizontal or vertical
                    orientation = input("Input 'Vertical' or 'Horizontal': ")
                    if orientation == 'Vertical' or orientation == 'Horizontal':
                        valid_orientation = True
                    else:
                        print("That's not a valid entry.")
                valid_square = False
                while not valid_square:  # This exists so that it'll keep trying every time you give it a bad orientation.
                    square = input("Enter the coordinates of the top-left square you want your ship to occupy in the form 'A1': ")  # ask player if they want it horizontal or vertical
                    if check_valid_coordinates(square):
                        valid_square = True
                    else:
                        print("That's not a valid square.")
                # ask for coordinates of top-left point
                if placement_is_valid(orientation, square, ship[1], matrix):
                    matrix = place_friendly_ship(orientation, square, ship[1], matrix)
                    print("You have placed your {} {}ly starting on square {}".format(ship[0], orientation.lower(), square))
                    dM.printBoard(matrix)
                    placed = True
    return matrix


def ship_placement_ai():  # The same, for the AI.
    print("I ain't done this shit yet")
    return


def board_is_clear(matrix):
    clear = True
    for row in range(1, len(matrix)):
        for cell in range(1, len(matrix[row])):
            if matrix[row][cell] != ' ':
                print("Problem with cell {} in row {}".format(cell, row))
                print("Board is not clear! If you're seeing this, the code's broken.")
                clear = False
    return clear


def placement_is_valid(orientation, square, length, matrix):  # Checks if placement overlaps other ships or the boundary
    if boundary_valid(orientation, square, length) and overlap_valid(orientation, square, length, matrix):
        valid = True
    else:
        valid = False
    return valid


def boundary_valid(orientation, square, length):  # Function that checks if the potential placement goes off the board.
    if orientation == 'Vertical':
        if coordinate_converter(square)[1] + length < 11:
            return True
        else:
            print("Ship goes beyond bottom of matrix")
            return False
    elif orientation == 'Horizontal':
        if coordinate_converter(square)[0] + length < 11:
            return True
        else:
            print("Ship goes beyond right side of matrix")
            return False
    else:
        print("How in the fuck did you get here with an invalid orientation")
        return False


def overlap_valid(orientation, square, length, matrix):  # Function that checks if the potential placement overlaps any other ships.
    cell = coordinate_converter(square)
    if orientation == 'Vertical':
        for i in range(0, length):
            if matrix[cell[0]][cell[1]+i] == 'O':
                print("Ship overlaps other ships")
                return False
        return True
    elif orientation == 'Horizontal':
        for i in range(0, length):
            if matrix[cell[0] + i][cell[1]] == 'O':
                print("Ship overlaps other ships")
                return False
        return True
    else:
        print("How in the fuck did you get here with an invalid orientation")
        return False


def check_valid_coordinates(square):  # Checks if a given string input is a valid square in the form 'A1'.
    if square[:1] in "ABCDEFGHIJ" and int(square[1:]) in range(1, 11):
        # print("{}{} is a valid set of coordinates. Checking validity of placement.".format(input[:1],input[1:]))
        valid = True
    else:
        print("{}{} is not a valid set of coordinates.".format(square[:1], square[1:]))
        valid = False
    return valid


def coordinate_converter(square):  # Takes A1 (as a string) and turns it into a tuple (0,0)
    column_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    if check_valid_coordinates(square):
        coordinates = ((column_dict[square[:1]]), (int(square[1:])-1))
        # print(coordinates)
        return coordinates
    else:
        print("Tried to convert invalid coordinates")


def place_friendly_ship(orientation, square, length, matrix):  # Takes all the variables listed and returns a matrix with the ship added.
    coords = coordinate_converter(square)
    if orientation == "Vertical":
        for i in range(0, length):
            matrix[coords[0]][coords[1]] = "O"
    elif orientation == "Horizontal":
        for i in range(0, length):
            matrix[coords[0]+i][coords[1]] = "O"
    else:
        print("Tried to place a ship with invalid orientation")
    return matrix


def place_ai_ship(orientation, square, length, matrix):  # Takes all the variables listed and returns a matrix with the ship added.
    return True


if __name__ == "__main__":
    ship_placement_player(playerBoard)

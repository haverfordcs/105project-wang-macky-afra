# This file governs ship placement for both the player and the AI. It will have to be imported to the game file in
# order for the game to be run.


def ship_placement_player(matrix):  # This function runs through the ship-placement sequence for the player. Call it
    # when you want the player to place their ships. It takes an empty matrix and lets the player fill it with ships.
    if not board_is_clear(matrix):  # if the board is empty
        print("Board is not clear!")
    else:
        ships_list = [('Aircraft Carrier', 5), ('Battleship', 4), ('Destroyer', 3), ('Submarine', 3), ('Patrol Boat', 2)]
        for ship in ships_list:
            print("You are placing your {}. It is {} squares long.".format(ship[0], ship[1]))  # Tell the player which ship they're placing and how long it is
            placed = False
            while not placed:  # This exists so that it'll keep trying every time you give it a bad placement.
                # print board so they can see where their ships are??
                valid_orientation = False
                while not valid_orientation:  #This exists so that it'll keep trying every time you give it a bad orientation.
                    print("Would you like to place your ship vertically or horizontally?")  # ask player if they want it horizontal or vertical
                    orientation = input("Input 'Vertical' or 'Horizontal': ")
                    if orientation == 'Vertical' or orientation == 'Horizontal':
                        valid_orientation = True
                    else:
                        print("That's not a valid entry.")
                valid_square = False
                while not valid_square:  #This exists so that it'll keep trying every time you give it a bad orientation.
                    square = input("Enter the coordinates of the top-left square you want your ship to occupy in the form 'A1': ")  # ask player if they want it horizontal or vertical
                    if check_valid_coordinates(square):
                        valid_square = True
                    else:
                        print("That's not a valid square.")
                # ask for coordinates of top-left point
                if placement_is_valid(orientation, square, ship[1]):
                    # place the ship
                    placed = True
    return matrix


def ship_placement_ai():  # The same, for the AI.
    print("I ain't done this shit yet")
    return


def board_is_clear(matrix): # Checks if the board is clear.
    clear = True
    if ((square != 'EMPTY' for square in row) for row in matrix):  # THIS NEEDS TO BE FIXED- CHANGE 'CLEAR' TO WHATEVER THE 'EMPTY' DATA VALUE IS
        clear = False
    return clear


def placement_is_valid(orientation, square, length):  # Checks if placement overlaps other ships or the boundary
    valid = True
    if ("it overlaps other ships"):
        valid = False
    elif ("it overlaps the boundary"):
        valid = False
    return valid


def check_valid_coordinates(input):  # Checks if a given input is a square in the form 'A1'.

    return


def test_input():
    thing = input("Say a thing at me: ")
    print(thing)
    return

test_input()


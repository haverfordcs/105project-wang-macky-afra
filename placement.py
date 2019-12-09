# This file governs ship placement for both the player and the AI. It will have to be imported to the game file in
# order for the game to be run.
import definingMatrices as dM
import random
# playerBoard = ([[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
# enemyBoard = ([[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])


def ship_placement_player(matrix):  # This function runs through the ship-placement sequence for the player. Call it
    # when you want the player to place their ships. It takes an empty matrix and lets the player fill it with ships.
    # Returns the matrix, and a dictionary of ship locations, in tuple form: (matrix, dict).
    player_ship_location_dict = {}
    playerIsLazy = input("Would you like to automatically place your ships? ").lower()
    if playerIsLazy == "yes":
        return ship_placement_lazy(matrix)
    if board_is_clear(matrix):
        ships_list = [('Aircraft Carrier', 5), ('Battleship', 4), ('Destroyer', 3), ('Submarine', 3), ('Patrol Boat', 2)]
        dM.printBoard(matrix)
        for ship in ships_list:
            placed = False
            while not placed:  # This exists so that it'll keep trying every time you give it a bad placement.
                print("You are placing your {}. It is {} squares long.".format(ship[0], ship[1]))  # Tell the player which ship they're placing and how long it is
                print("Would you like to place your ship vertically or horizontally?")  # ask player if they want it horizontal or vertical
                orientation = input("Input 'Vertical' or 'Horizontal': ").lower()
                if orientation == 'vertical' or orientation == 'horizontal':
                    square = input("Enter the coordinates of the top-left square you want your ship to occupy in the form 'A0': ")  # ask player if they want it horizontal or vertical
                    if check_valid_coordinates(square):
                        if placement_is_valid(orientation, square, ship[1], matrix, "Player"):
                            matrix, player_ship_location_dict = place_friendly_ship(orientation, square, ship[1], matrix, ship[0], player_ship_location_dict)
                            dM.printBoard(matrix)
                            print("You have placed your {} {}ly starting on square {}".format(ship[0], orientation, square))
                            placed = True
                    else:
                        print("That's not a valid entry. Try again!")
                else:
                    print("That's not a valid entry. Try again!")
        print("You have finished placing your ships!")
    else:
        print("Board is not clear!")
    return matrix, player_ship_location_dict


def ship_placement_ai(matrix):  # This function runs through the ship-placement sequence for the ai. Call it
    # when you want the AI to place their ships. It takes an empty matrix and automatically fills it with ships.
    # Returns the matrix, and a dictionary of ship locations, in tuple form: (matrix, dict).
    ai_ship_location_dict = {}
    if board_is_clear(matrix):
        ships_list = [('Aircraft Carrier', 5), ('Battleship', 4), ('Destroyer', 3), ('Submarine', 3), ('Patrol Boat', 2)]
        bad_ideas = []
        for ship in ships_list:
            placed = False
            while not placed:  # This exists so that it'll keep trying every time you give it a bad placement.
                # dM.printBoard(matrix)
                # print("You are placing your {}. It is {} squares long.".format(ship[0], ship[1]))  # Tell the player which ship they're placing and how long it is
                # print("Would you like to place your ship vertically or horizontally?")  # ask player if they want it horizontal or vertical
                # orientation = input("Input 'Vertical' or 'Horizontal': ")
                orientationdict = {0: "Vertical", 1: "Horizontal"}
                orientation = orientationdict[random.randint(0, 1)].lower()
                # square = input("Enter the coordinates of the top-left square you want your ship to occupy in the form 'A1': ")  # ask player if they want it horizontal or vertical
                columndict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
                square = ""+str(columndict[random.randint(0, 9)])+str(random.randint(0, 9))
                if placement_is_valid(orientation, square, ship[1], matrix, "AI"):
                    good_idea = False
                    if orientation == "vertical" and (orientation, coordinate_converter(square)[1]) not in bad_ideas:
                        good_idea = True
                    elif orientation == "horizontal" and (orientation, coordinate_converter(square)[0]) not in bad_ideas:
                        good_idea = True
                    if good_idea:
                        matrix, ai_ship_location_dict = place_enemy_ship(orientation, square, ship[1], matrix, ship[0], ai_ship_location_dict)
                        # print("The AI has placed their {} {}ly starting on square {}".format(ship[0], orientation.lower(), square))
                        if orientation == "vertical":
                            bad_ideas.append((orientation, coordinate_converter(square)[1]))
                            bad_ideas.append((orientation, coordinate_converter(square)[1]-1))
                            bad_ideas.append((orientation, coordinate_converter(square)[1]+1))
                        else:
                            bad_ideas.append((orientation, coordinate_converter(square)[0]))
                            bad_ideas.append((orientation, coordinate_converter(square)[0] - 1))
                            bad_ideas.append((orientation, coordinate_converter(square)[0] + 1))
                        placed = True
        #             else:
        #                 print("That's not a valid entry.")
        #         else:
        #             print("That's not a valid entry.")
        # print("You have finished placing your ships!")
    else:
        print("Board is not clear!")
    return matrix, ai_ship_location_dict

def ship_placement_lazy(matrix):
    player_ship_location_dict = {}
    if board_is_clear(matrix):
        ships_list = [('Aircraft Carrier', 5), ('Battleship', 4), ('Destroyer', 3), ('Submarine', 3),
                      ('Patrol Boat', 2)]
        bad_ideas = []
        for ship in ships_list:
            placed = False
            while not placed:  # This exists so that it'll keep trying every time you give it a bad placement.
                # dM.printBoard(matrix)
                # print("You are placing your {}. It is {} squares long.".format(ship[0], ship[1]))  # Tell the player which ship they're placing and how long it is
                # print("Would you like to place your ship vertically or horizontally?")  # ask player if they want it horizontal or vertical
                # orientation = input("Input 'Vertical' or 'Horizontal': ")
                orientationdict = {0: "Vertical", 1: "Horizontal"}
                orientation = orientationdict[random.randint(0, 1)].lower()
                # square = input("Enter the coordinates of the top-left square you want your ship to occupy in the form 'A1': ")  # ask player if they want it horizontal or vertical
                columndict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
                square = "" + str(columndict[random.randint(0, 9)]) + str(random.randint(0, 9))
                if placement_is_valid(orientation, square, ship[1], matrix, "AI"):
                    good_idea = False
                    if orientation == "vertical" and (orientation, coordinate_converter(square)[1]) not in bad_ideas:
                        good_idea = True
                    elif orientation == "horizontal" and (
                    orientation, coordinate_converter(square)[0]) not in bad_ideas:
                        good_idea = True
                    if good_idea:
                        matrix, player_ship_location_dict = place_lazy_ship(orientation, square, ship[1], matrix, ship[0],
                                                                         player_ship_location_dict)
                        # print("The AI has placed their {} {}ly starting on square {}".format(ship[0], orientation.lower(), square))
                        if orientation == "vertical":
                            bad_ideas.append((orientation, coordinate_converter(square)[1]))
                            bad_ideas.append((orientation, coordinate_converter(square)[1] - 1))
                            bad_ideas.append((orientation, coordinate_converter(square)[1] + 1))
                        else:
                            bad_ideas.append((orientation, coordinate_converter(square)[0]))
                            bad_ideas.append((orientation, coordinate_converter(square)[0] - 1))
                            bad_ideas.append((orientation, coordinate_converter(square)[0] + 1))
                        placed = True
        #             else:
        #                 print("That's not a valid entry.")
        #         else:
        #             print("That's not a valid entry.")
        # print("You have finished placing your ships!")
    else:
        print("Board is not clear!")
    return matrix, player_ship_location_dict


def board_is_clear(matrix):
    clear = True
    for row in range(1, len(matrix)):
        for cell in range(1, len(matrix[row])):
            if matrix[row][cell] != ' ':
                print("Problem with cell {} in row {}".format(cell, row))
                print("Board is not clear! If you're seeing this, the code's broken.")
                clear = False
    return clear


def placement_is_valid(orientation, square, length, matrix, identity):  # Checks if placement overlaps other ships or the boundary
    if boundary_valid(orientation, square, length, identity) and overlap_valid(orientation, square, length, matrix, identity):
        valid = True
    else:
        valid = False
    return valid


def boundary_valid(orientation, square, length, identity):  # Function that checks if the potential placement goes off the board.
    # print("Checking boundary validity...")
    if orientation == 'vertical':
        if coordinate_converter(square)[0] + length < 11:
            # print("Placement is on board")
            return True
        else:
            if identity == "Player":
                print("Ship goes beyond bottom of matrix. Placement is invalid.")
            return False
    elif orientation == 'horizontal':
        if coordinate_converter(square)[1] + length < 11:
            # print("Placement is on board")
            return True
        else:
            if identity == "Player":
                print("Ship goes beyond right side of matrix. Placement is invalid.")
            return False
    else:
        print("Invalid orientation detected in boundary_valid")
        return False


def overlap_valid(orientation, square, length, matrix, identity):  # Function that checks if the potential placement overlaps any other ships.
    cell = coordinate_converter(square)
    # print("Checking overlap validity...")
    if orientation == 'vertical':
        for i in range(0, length):
            if matrix[cell[0]+i][cell[1]] in "OI":
                if identity == "Player":
                    print("Ship overlaps other ships. Placement is invalid.")
                return False
        # print("No overlaps detected")
        return True
    elif orientation == 'horizontal':
        for i in range(0, length):
            if matrix[cell[0]][cell[1]+i] in "OI":
                if identity == "Player":
                    print("Ship overlaps other ships. Placement is invalid.")
                return False
        # print("No overlaps detected")
        return True
    else:
        print("Invalid orientation found in overlap_valid")
        return False


def check_valid_coordinates(square):  # Checks if a given string input is a valid square in the form 'A0'.
    if square[:1].upper() in "ABCDEFGHIJ" and square[1:] in "0123456789":
        # print("{}{} is a valid set of coordinates. Checking validity of placement.".format(input[:1],input[1:]))
        return True
    else:
        # print("{}{} is not a valid set of coordinates.".format(square[:1], square[1:]))
        return False


def coordinate_converter(square):  # Takes A0 (as a string) and turns it into a tuple (0,0) with row first
    column_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    if check_valid_coordinates(square):
        coordinates = ((int(square[1:])), (column_dict[square[:1].upper()]))
        # print(coordinates)
        return coordinates
    else:
        print("Tried to convert invalid coordinates")


def place_friendly_ship(orientation, square, length, matrix, ship_name, player_ship_location_dict):  # Takes all the variables listed and returns a tuple: the first element is a matrix with the ship added, the second is an updated ships_location_dict.
    coords = coordinate_converter(square)
    cells = []
    if orientation == "vertical":
        for i in range(0, length):
            # print("Placing at coordinates ({}, {})".format(coords[0]+i, coords[1]))
            matrix[coords[0]+i][coords[1]] = "O"
            cells.append((coords[0]+i, coords[1]))
    elif orientation == "horizontal":
        for i in range(0, length):
            # print("Placing at coordinates ({}, {})".format(coords[0], coords[1]+i))
            matrix[coords[0]][coords[1]+i] = "O"
            cells.append((coords[0], coords[1]+i))
    else:
        print("Tried to place a ship with invalid orientation")
    player_ship_location_dict[ship_name] = cells
    # print(player_ship_location_dict)
    return matrix, player_ship_location_dict


def place_enemy_ship(orientation, square, length, matrix, ship_name, ai_ship_location_dict):  # Takes all the variables listed and returns a tuple: the first element is a matrix with the ship added, the second is an updated ships_location_dict.
    coords = coordinate_converter(square)
    cells = []
    if orientation == "vertical":
        for i in range(0, length):
            # print("Placing at coordinates ({}, {})".format(coords[0]+i, coords[1]))
            matrix[coords[0]+i][coords[1]] = "I"
            cells.append((coords[0]+i, coords[1]))
    elif orientation == "horizontal":
        for i in range(0, length):
            # print("Placing at coordinates ({}, {})".format(coords[0], coords[1]+i))
            matrix[coords[0]][coords[1]+i] = "I"
            cells.append((coords[0], coords[1]+i))
    else:
        print("Tried to place a ship with invalid orientation")
    ai_ship_location_dict[ship_name] = cells
    # print(player_ship_location_dict)
    return matrix, ai_ship_location_dict


def place_lazy_ship(orientation, square, length, matrix, ship_name, player_ship_location_dict):  # Takes all the variables listed and returns a tuple: the first element is a matrix with the ship added, the second is an updated ships_location_dict.
    coords = coordinate_converter(square)
    cells = []
    if orientation == "vertical":
        for i in range(0, length):
            # print("Placing at coordinates ({}, {})".format(coords[0]+i, coords[1]))
            matrix[coords[0]+i][coords[1]] = "O"
            cells.append((coords[0]+i, coords[1]))
    elif orientation == "horizontal":
        for i in range(0, length):
            # print("Placing at coordinates ({}, {})".format(coords[0], coords[1]+i))
            matrix[coords[0]][coords[1]+i] = "O"
            cells.append((coords[0], coords[1]+i))
    else:
        print("Tried to place a ship with invalid orientation")
    player_ship_location_dict[ship_name] = cells
    # print(player_ship_location_dict)
    return matrix, player_ship_location_dict


if __name__ == "__main__":
    player_board, player_dict = ship_placement_player(playerBoard)
    ai_board, ai_dict = ship_placement_ai(enemyBoard)
    dM.printBothBoards(player_board, ai_board)
    dM.printBothBoards(player_board, dM.hideHidden(ai_board))

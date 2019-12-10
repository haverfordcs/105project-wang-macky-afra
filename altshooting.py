import random
from shooting import *
from CheckSink import *

target = ()  # This will be filled when it has a target.
direction_list = random.randint(1, 2)  # Randomizes which direction it tries first. Rerandomizes after every sink.
# directionDict = {1: "Right", 2: "Up"}
# print("Direction set to {}".format(directionDict[direction_list]))


def altEnemyShot(playerBoard, enemyBoard, player_ship_location_dict):
    global target
    global direction_list
    firing = 1
    while firing:  # Loop so it will retry in the event of a failed shot
        # print("Checking for target")

        # checking if target has sunk
        if target:  # i.e. if there's a target.
            if playerBoard[target[0]][target[1]] == "V":  # Checks if the target is sunk- if it is, clears target and rerandomizes direction.
                # print("Target at", target, "sunk!")
                target = ()
                direction_list = random.randint(1, 2)
                directionDict = {1: "Right", 2: "Up"}
                # print("Target sunk. Direction set to {}".format(directionDict[direction_list]))

        if not target:  # If there's no target, needs to check for a new one.
            # print("No target yet. Checking for new target!")
            is_new_target, target = targetScan(playerBoard)  # Checks for a new target. If there is, returns True and the target.
            if not is_new_target:  # i.e. there is no new target, so it will have to shoot randomly.
                # print("No new target found. Firing randomly.")
                # random shot
                row = random.randint(0, 9)
                column = random.randint(0, 9)

                # Hit
                if playerBoard[row][column] == "O":
                    playerBoard[row][column] = "X"
                    ship, sunk = check_sink(player_ship_location_dict, playerBoard)
                    printBothBoards(playerBoard, hideHidden(enemyBoard))
                    print("Enemy hit!")
                    if sunk:
                        print("The enemy sunk your {}!".format(ship))

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
                    # print("Already fired here.")
                    firing = 1

        elif target:  # If there's a target to shoot at
            # print("Target locked at {}.".format(target))
            if direction_list == 1:  # It's going Right first
                # print("Direction is RLUD")
                for direction in ['right', 'left', 'up', 'down']:  # Checks each direction in order.
                    # print("Checking {} from target".format(direction))
                    if check_direction(direction, playerBoard, target):  # If there's somewhere to shoot in that direction...
                        # print("Shooting {} from target!".format(direction))
                        shoot(direction, playerBoard, target, enemyBoard, player_ship_location_dict)  # It shoots there.
                        firing = 0
                        break
            elif direction_list == 2:  # It's going Up first
                # print("Direction is UDRL")
                for direction in ['up', 'down', 'right', 'left']:  # Checks each direction in order.
                    # print("Checking {} from target".format(direction))
                    if check_direction(direction, playerBoard, target):  # If there's somewhere to shoot in that direction...
                        # print("Shooting {} from target!".format(direction))
                        shoot(direction, playerBoard, target, enemyBoard, player_ship_location_dict)  # It shoots there.
                        firing = 0
                        break
            else:
                print("The direction's messed up. It looks like this:")  # Just in case something goes wrong, this is an error report.
                print(direction_list)

            if firing == 1:
                print("Something odd happened. None of the directions worked. Clearing target.")  # If it has a target with no possible directions, it resets.
                target = ()
                direction_list = random.randint(1, 2)


def targetScan(board):  # Scans a board for targets (data value X).
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                # print("New target found!")
                return True, (i, j)
    return False, ()


def check_direction(direction, playerBoard, target):  # Checks if there's somewhere to shoot in a direction. Returns 'true' if there is a blank space after any number of X's, returns False otherwise.
    row = target[0]
    column = target[1]
    if direction == 'right':  # for each direction, check if it's at the edge, then if there's a blank space.
        column += 1  # Switches to observing the cell to the right
        if column == 10:  # It's off the end of the board
            return False
        if playerBoard[row][column] == "X":  # There's a hit
            return check_direction(direction, playerBoard, (row, column))  # Check the next one over
        if playerBoard[row][column] == "+":  # There's a miss
            return False  # the direction's done
        if playerBoard[row][column] == "V":  # There's a sunken ship
            return False  # the direction's done
        else:  # There's a blank space
            return True  # Shoot this way!

    elif direction == 'left':  # See 'right'
        column -= 1
        if column == -1:
            return False
        if playerBoard[row][column] == "X":
            return check_direction(direction, playerBoard, (row, column))
        if playerBoard[row][column] == "+":
            return False
        if playerBoard[row][column] == "V":
            return False
        else:
            return True

    elif direction == 'up':  # See 'right'
        row -= 1
        if row == -1:
            return False
        if playerBoard[row][column] == "X":
            return check_direction(direction, playerBoard, (row, column))
        if playerBoard[row][column] == "+":
            return False
        if playerBoard[row][column] == "V":
            return False
        else:
            return True

    elif direction == 'down':  # See 'right'
        row += 1
        if row == 10:
            return False
        if playerBoard[row][column] == "X":
            return check_direction(direction, playerBoard, (row, column))
        if playerBoard[row][column] == "+":
            return False
        if playerBoard[row][column] == "V":
            return False
        else:
            return True


def shoot(direction, playerBoard, target, enemyBoard, player_ship_location_dict):  # Shoots in the earliest available blank space in a direction
    row = target[0]
    column = target[1]
    if direction == 'right':
        column += 1  # shift to the right
        # Hit
        if playerBoard[row][column] == "O":  # If there's a ship
            playerBoard[row][column] = "X"
            ship, sunk = check_sink(player_ship_location_dict, playerBoard)
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy hit!")
            if sunk:
                print("The enemy sunk your {}!".format(ship))

        # Miss
        elif playerBoard[row][column] == " ":  # if there's empty space
            playerBoard[row][column] = "+"
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy miss!")

        elif playerBoard[row][column] == "X":  # If there's a hit already
            shoot(direction, playerBoard, (row, column), enemyBoard, player_ship_location_dict)  # Move over to the next one and try shooting there

    elif direction == 'left':  # See 'right'
        column -= 1
        # Hit
        if playerBoard[row][column] == "O":
            playerBoard[row][column] = "X"
            ship, sunk = check_sink(player_ship_location_dict, playerBoard)
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy hit!")
            if sunk:
                print("The enemy sunk your {}!".format(ship))

        # Miss
        elif playerBoard[row][column] == " ":
            playerBoard[row][column] = "+"
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy miss!")

        elif playerBoard[row][column] == "X":
            shoot(direction, playerBoard, (row, column), enemyBoard, player_ship_location_dict)

    elif direction == 'up':  # See 'right'
        row -= 1
        # Hit
        if playerBoard[row][column] == "O":
            playerBoard[row][column] = "X"
            ship, sunk = check_sink(player_ship_location_dict, playerBoard)
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy hit!")
            if sunk:
                print("The enemy sunk your {}!".format(ship))

        # Miss
        elif playerBoard[row][column] == " ":
            playerBoard[row][column] = "+"
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy miss!")

        elif playerBoard[row][column] == "X":
            shoot(direction, playerBoard, (row, column), enemyBoard, player_ship_location_dict)

    elif direction == 'down':  # See 'right'
        row += 1
        # Hit
        if playerBoard[row][column] == "O":
            playerBoard[row][column] = "X"
            ship, sunk = check_sink(player_ship_location_dict, playerBoard)
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy hit!")
            if sunk:
                print("The enemy sunk your {}!".format(ship))

        # Miss
        elif playerBoard[row][column] == " ":
            playerBoard[row][column] = "+"
            printBothBoards(playerBoard, hideHidden(enemyBoard))
            print("Enemy miss!")

        elif playerBoard[row][column] == "X":
            shoot(direction, playerBoard, (row, column), enemyBoard, player_ship_location_dict)

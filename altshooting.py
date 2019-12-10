import random
from shooting import *
from CheckSink import *

target = ()
direction_list = random.randint(1, 2)
directionDict = {1: "Right", 2: "Up"}
# print("Direction set to {}".format(directionDict[direction_list]))


def altEnemyShot(playerBoard, enemyBoard, player_ship_location_dict):
    global target
    global direction_list
    firing = 1
    while firing:
        # print("Checking for target")

        # checking if target has sunk
        if target:
            if playerBoard[target[0]][target[1]] == "V":
                # print("Target at", target, "sunk!")
                target = ()
                direction_list = random.randint(1, 2)
                directionDict = {1: "Right", 2: "Up"}
                # print("Target sunk. Direction set to {}".format(directionDict[direction_list]))

        if not target:
            # print("No target yet. Checking for new target!")
            is_new_target, target = targetScan(playerBoard)
            if not is_new_target:
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

        elif target:
            # print("Target locked at {}.".format(target))
            if direction_list == 1:
                # print("Direction is RLUD")
                for direction in ['right', 'left', 'up', 'down']:
                    print("Checking {} from target".format(direction))
                    if check_direction(direction, playerBoard, target):
                        print("Shooting {} from target!".format(direction))
                        shoot(direction, playerBoard, target, enemyBoard, player_ship_location_dict)
                        firing = 0
                        break
            elif direction_list == 2:
                # print("Direction is UDRL")
                for direction in ['up', 'down', 'right', 'left']:
                    print("Checking {} from target".format(direction))
                    if check_direction(direction, playerBoard, target):
                        print("Shooting {} from target!".format(direction))
                        shoot(direction, playerBoard, target, enemyBoard, player_ship_location_dict)
                        firing = 0
                        break
            else:
                print("The direction's messed up. It looks like this:")
                print(direction_list)

            if firing == 1:
                print("Something odd happened. None of the directions worked. Clearing target.")
                target = ()
                direction_list = random.randint(1, 2)


def targetScan(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                # print("New target found!")
                return True, (i, j)
    return False, ()


def check_direction(direction, playerBoard, target):
    row = target[0]
    column = target[1]
    if direction == 'right': # for each direction, check if it's at the edge, then if there's a blank space.
        column += 1
        if column == 10:
            return False
        if playerBoard[row][column] == "X":
            return check_direction(direction, playerBoard, (row, column))
        if playerBoard[row][column] == "+":
            return False
        if playerBoard[row][column] == "V":
            return False
        else:
            return True

    elif direction == 'left':
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

    elif direction == 'up':
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

    elif direction == 'down':
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


def shoot(direction, playerBoard, target, enemyBoard, player_ship_location_dict):
    row = target[0]
    column = target[1]
    if direction == 'right':
        column += 1
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

    elif direction == 'left':
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

    elif direction == 'up':
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

    elif direction == 'down':
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

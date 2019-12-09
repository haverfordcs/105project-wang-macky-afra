from placement import *
from definingMatrices import *
from placement import *
from shooting import *
from start_game import *
from CheckWin import *
from CheckSink import *
import random



def Battleship():
    Start()
    playerBoard = (
    [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
    enemyBoard = (
    [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
    playerBoard, player_ship_location_dict = ship_placement_player(playerBoard)
    enemyBoard, ai_ship_location_dict = ship_placement_ai(enemyBoard)
    playerFirst = RockPaperScissors()
    printBothBoards(playerBoard, hideHidden(enemyBoard))
    if playerFirst == True:
        playerShot(playerBoard, enemyBoard)
    while check_win(playerBoard, "Player") == False and check_win(enemyBoard, "AI") == False:
        enemyShot(playerBoard, enemyBoard, loopCount)
        for ship in player_ship_location_dict:
            if check_sink(ship, player_ship_location_dict, playerBoard) == True:
                cells = player_ship_location_dict[ship]
                for cell in cells:
                    playerBoard[cell[0]][cell[1]] = 'V'
                print("Your ship has sunk!")
        playerShot(playerBoard, enemyBoard)
        for ship in ai_ship_location_dict:
            if check_sink(ship, ai_ship_location_dict, enemyBoard) == True:
                cells = ai_ship_location_dict[ship]
                for cell in cells:
                    enemyBoard[cell[0]][cell[1]] = 'V'

                print("You sunk an enemy ship!")
    if check_win(enemyBoard, "AI"):
        print("Congratulations! You have won at Battleships!")
    else:
        print("You have lost! Better luck next time!")
Battleship()

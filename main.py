from placement import *
from definingMatrices import *
from placement import *
from shooting import *
from start_game import *
from CheckWin import *
from CheckSink import *
from altshooting import *
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
    if playerFirst == True:
        printBothBoards(playerBoard, hideHidden(enemyBoard))
        playerShot(playerBoard, enemyBoard, ai_ship_location_dict)
        x = input("Press enter to continue")
    while check_win(playerBoard, "Player") == False and check_win(enemyBoard, "AI") == False:
        altEnemyShot(playerBoard, enemyBoard, player_ship_location_dict)
        playerShot(playerBoard, enemyBoard, ai_ship_location_dict)
        x = input("Press enter to continue")
    if check_win(enemyBoard, "AI"):
        print("Congratulations! You have won at Battleships!")
    else:
        print("You have lost! Better luck next time!")


Battleship()

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
    Start()  # Displays the rules
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
    playerBoard, player_ship_location_dict = ship_placement_player(playerBoard)  # The player places their ships.
    enemyBoard, ai_ship_location_dict = ship_placement_ai(enemyBoard)  # The AI places their ships.
    if RockPaperScissors():  # Returns True if the player wins Rock, Paper, Scissors.
        printBothBoards(playerBoard, hideHidden(enemyBoard))  # After this, the printing happens inside the playerShot and altEnemyShot functions.
        playerShot(playerBoard, enemyBoard, ai_ship_location_dict)  # The player shoots.
        x = input("Press enter to continue")  # To prevent the AI from instantly shooting
    while check_win(playerBoard) == False and check_win(enemyBoard) == False:  # While nobody has won
        altEnemyShot(playerBoard, enemyBoard, player_ship_location_dict)  # The AI shoots
        playerShot(playerBoard, enemyBoard, ai_ship_location_dict)  # Then the player shoots
        x = input("Press enter to continue")  # To prevent the AI from instantly shooting
    if check_win(enemyBoard):  # Check_win checks to see if a board's ships are all sunk. If the enemyBoard's ships are sunk, the player has won.
        print("Congratulations! You have won at Battleships!")
    else:  # i.e. the AI has won.
        print("You have lost! Better luck next time!")


Battleship()

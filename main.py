from placement import *
from definingMatrices import *
from placement import *
from shooting import *
from start_game import *
from CheckWin import *
from CheckSink import *



def Battleship():
    Start()
    global playerBoard
    global enemyBoard
    playerBoard, player_ship_location_dict = ship_placement_player(playerBoard)
    enemyBoard, ai_ship_location_dict = ship_placement_ai(enemyBoard)
    First_player = RockPaperScissors()
    while check_win(playerBoard, "Player") == False and check_win(enemyBoard, "AI") == False :
        printBothBoards(playerBoard, hideHidden(enemyBoard))
        playerShot(enemyBoard)
        #enemyshooting
        for ship in ai_ship_location_dict:
            if check_sink(ship, ai_ship_location_dict, enemyBoard) == True:
                cells = ai_ship_location_dict[ship]
                for cell in cells:
                    enemyBoard[cell[0]][cell[1]] = 'V'
        for ship in player_ship_location_dict:
            if check_sink(ship, player_ship_location_dict, playerBoard) == True:
                cells = player_ship_location_dict[ship]
                for cell in cells:
                    playerBoard[cell[0]][cell[1]] = 'V'

Battleship()

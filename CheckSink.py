


def check_sink(ship, ship_location_dict, board):
    #This function goes through ship_location_dict for AI/Player and checks to see if ships have been sunk
    cells = ship_location_dict[ship]
    for cell in cells:
        if board[cell[0]][cell[1]] != 'X':
            #if all tuples of coodrinates are not 'X' then the ship has not been sunk
            return False
    return True


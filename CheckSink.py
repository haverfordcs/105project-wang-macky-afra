def check_sink(ship_location_dict, board):
    # This function goes through ship_location_dict for AI/Player and checks to see if ships have been sunk
    for ship in ship_location_dict:
        sunk = True
        for cell in ship_location_dict[ship]:
            if board[cell[0]][cell[1]] != 'X':
                # If any cell's data value is not X, the ship has not been sunk.
                sunk = False
        if sunk:
            for cell in ship_location_dict[ship]:
                board[cell[0]][cell[1]] = "V"
            return ship, sunk  # Used to print sink messages if 'sunk' is true
    return "nothing", False


def check_win(board):
    # This function checks for the winner by evaluating the board. If the board is clear, the other player has won.
    win = True
    for i in range(10):
        for j in range(10):
            if board[i][j] in "OI":
                # if a cell contains a ship then return False
                win = False
    return win



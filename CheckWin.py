def check_win(board, winner):
    #This function checks for the winner by evaluating the board
    #if any cell on player's board still contains O and any cell on AI's board contains I, then no one has won yet
    if winner == "Player":
       ship = 'O'
    else:
       ship = 'I'
    win = True
    for i in range(10):
       for j in range(10):
           if board[i][j] == ship:
               #if a cell contains a hidden ship then return False
               win = False
    return win



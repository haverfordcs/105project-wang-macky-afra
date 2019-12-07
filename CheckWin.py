def check_win(board, winner):
    #This function checks for the winner by evaluating the board
   #if any cell on player's board still contains O and any cell on AI's board contains I, then no one has won yet
   win = 'O' if winner == "Player" else 'I'
   for i in range(10):
       for j in range(10):
           if board[i][j] == win:
               #if a cell contains a hidden ship then return False
               return False
           else:
               #if there are no hidden ships then return True
               #print("Congratulations! You won battleship!")
               return True



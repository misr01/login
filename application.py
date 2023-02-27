def board(height,width): #generates board
    boardheight = []
    for x in range(height): #creates columns
        boardheight.append([])
        for i in range(width): #creates arrays with  blank spaces, each array is 1 row
            boardheight[x].append("-")
    return boardheight #returns created array(board)



height = int(input("Enter height of board"))
width = int(input("Enter width of board"))
boardreal = board(height,width) #this contains the board

for i in range(height * width):
    if i % 2 == 0:
        #PositionPlayer1
        p1Height = int(input("Enter your column position Player1"))
        p1Width = int(input("Enter  your row position Player1"))
        while boardreal[p1Height][p1Width] == "x" or boardreal[p1Height][p1Width] == "o":
            p1Height = int(input("Not possible, enter your column position Player1"))
            p1Width = int(input("Not possible, enter your row position Player1"))
        boardreal[p1Height][p1Width] = "x"
        print(boardreal)
    else:
    #PositionPlayer2
        p2Height = int(input("Enter your column position Player2"))
        p2Width = int(input("Enter  your row position Player2"))
        while boardreal[p2Height][p2Width] == "x" or boardreal[p2Height][p2Width] == "o":
            p2Height = int(input("Not possible, enter your column position Player2"))
            p2Width = int(input("Not possible, enter your row position Player2"))
        boardreal[p2Height][p2Width] = "o"
        print(boardreal)

############ with win condiiton

def board(height,width): #generates board
    boardheight = []
    for x in range(height): #creates columns
        boardheight.append([])
        for i in range(width): #creates arrays with  blank spaces, each array is 1 row
            boardheight[x].append("-")
    return boardheight #returns created array(board)

def check_win(board, symbol):
    # check rows for win
    for row in board:
        if all(val == symbol for val in row):
            return True

    # check columns for win
    for col in range(len(board[0])):
        if all(board[row][col] == symbol for row in range(len(board))):
            return True

    # check diagonals for win
    if all(board[i][i] == symbol for i in range(len(board))):
        return True
    if all(board[i][len(board) - i - 1] == symbol for i in range(len(board))):
        return True

    return False

def check_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

height = int(input("Enter height of board: "))
width = int(input("Enter width of board: "))
boardreal = board(height,width) #this contains the board

for i in range(height * width):
    if i % 2 == 0:
        #PositionPlayer1
        p1Height = int(input("Enter your column position Player1: "))
        p1Width = int(input("Enter  your row position Player1: "))
        while boardreal[p1Height][p1Width] == "x" or boardreal[p1Height][p1Width] == "o":
            p1Height = int(input("Not possible, enter your column position Player1: "))
            p1Width = int(input("Not possible, enter your row position Player1: "))
        boardreal[p1Height][p1Width] = "x"
        if check_win(boardreal, "x"):
            print("Player 1 wins!")
            break
        elif check_full(boardreal):
            print("It's a draw!")
            break
        print(boardreal)
    else:
        #PositionPlayer2
        p2Height = int(input("Enter your column position Player2: "))
        p2Width = int(input("Enter  your row position Player2: "))
        while boardreal[p2Height][p2Width] == "x" or boardreal[p2Height][p2Width] == "o":
            p2Height = int(input("Not possible, enter your column position Player2: "))
            p2Width = int(input("Not possible, enter your row position Player2: "))
        boardreal[p2Height][p2Width] = "o"
        if check_win(boardreal, "o"):
            print("Player 2 wins!")
            break
        elif check_full(boardreal):
            print("It's a draw!")
            break

'''This is a TicTacToe Game played with computer.
Computer always make the first move with mark 'X'
at the center of the board. The User Input is
registered with a mark 'O' on the board '''

from random import randrange


def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

    boardShape1 = ('+' + 7*'-')*3 + '+' + '\n' + '|' + (" "*7 + '|')*3 + '\n' + '|' + " "*3 + board[0][0]

    boardShape2 = " "*3 + '|' + " "*3 + board[0][1]


    boardShape3 = " "*3 + '|' + " "*3 + board[0][2]


    boardShape4 = " "*3 + '|' + '\n' + ('|' + " "*7)*3 + '|' +  '\n' + ('+' + '-'*7)*3 + '+' + '\n' + ('|' + " "*7)*3 + '|' + '\n' + '|' + " "*3 + board[1][0]



    boardShape5 = " "*3 + '|' + " "*3 + board[1][1]


    boardShape6 = " "*3 + '|' + " "*3 + board[1][2]


    boardShape7 = " "*3 + '|' + '\n' + ('|' + " "*7)*3  + '|' + '\n' + ('+' + 7*'-')*3 + '+' + '\n' + ('|' + " "*7)*3  + '|' + '\n' + '|' +" "*3 + board[2][0]

    boardShape8 = " "*3 + '|' + " "*3 + board[2][1]


    boardShape9 = " "*3 + '|' + " "*3 + board[2][2] +  " "*3 + '|' +  '\n'  +  ('|' + " "*7)*3 + '|' +  '\n' + ('+' + '-'*7)*3  + '+'

    boardShape  = boardShape1 + boardShape2 +boardShape3 + boardShape4 + boardShape5 + boardShape6 + boardShape7 + boardShape8 + boardShape9
            
    print(boardShape)

    
def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    userInput = input("Enter your move: ")
    while(userInput not in freeBoardNumber):
        userInput = input("Enter your move: ")
        
    for row in range(3):
        for column in range(3):
            if (board[row][column] == str(userInput)):
                board[row][column] = 'O'
    freeBoardNumber.remove(userInput)
                             
    DisplayBoard(board)
        

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    listOfFreeFields = []

    for row in range(3):
        for column in range(3):
                if(board[row][column] in freeBoardNumber):
                    listOfFreeFields.append((row,column))
    print("List Of Free Fields: ",listOfFreeFields)


def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    # Horizontal win
    for row in board:
        if (row.count(sign)==len(board)):
                return True
            
    # Vertical win
##    for row in range(3):
##        if (row == 1):
##            break
##        for column in range(3):
##            if ((board[row][column] == board[row+1][column] == board[row+2][column]==sign) and (row ==0)):
##                return True
    for column in range(len(board[0])):
        checkColumn = []
        for row in board:
            checkColumn.append(row[column])
        if (checkColumn.count(sign) == len(checkColumn)):
            return True
            
    # Diagonal win
##    for row in range(3):
##        if (row == 1):
##            break
##        for column in range(3):
##            if (column == 1):
##                break
##            if (((board[row][column]==board[row+1][column+1]==board[row+2][column+2]==sign) or (board[row][column+2]==board[row+1][column+1]==board[row+2][column]==sign))and row==0):
##                    return True
    # Diagonal win (\)
    diag = []
    for rowcol in range(len(board)):
        diag.append(board[rowcol][rowcol])
        
    if(diag.count(sign) == len(diag)):
        return True

    # Diagonal win (/)
    diag = []
    for row, reversed_col in enumerate(reversed(range(len(board)))):
        diag.append(board[row][reversed_col])

    if(diag.count(sign) == len(diag)):
        return True

    
def DrawMove(board): # This function draws computer move
    #The first move belongs to the computer. It puts 'X' in the middle of the board
#
# the function draws the computer's move and updates the board
#

# The first move belongs to the computer and it places 'X' in the middle of the board
    if(len(freeBoardNumber)==9):
        board[1][1]  = 'X'
        freeBoardNumber.remove('5')
        
    else:
        computerNumber = 5
        while(str(computerNumber) not in freeBoardNumber):
            computerNumber = 1 + randrange(9)
            
        for row in range(3):
            for column in range(3):
                if board[row][column] == str(computerNumber):
                    board[row][column] = 'X'
        freeBoardNumber.remove(str(computerNumber))

    DisplayBoard(board)


def GameIsNotOver():
    if (VictoryFor(board, 'X') and VictoryFor(board,'O') ):
        print("It is a tie between You and Computer!")
        return False
    
    elif (VictoryFor(board, 'X')):
        print("Computer won!")
        return False
               
    elif (VictoryFor(board, 'O')):
        print("You won!")
        return False
    
    elif (len(freeBoardNumber)!=1):
        return True
    
    else:
        print("There is no winner between You and Computer. Game is over!")
        return False
    
    
if(__name__ == "__main__"):
    print(__doc__)
print()

board = [['1','2','3'],['4','5','6'],['7','8','9']]

freeBoardNumber = [str(i+1) for i in range(9)]

while(GameIsNotOver()):
    DrawMove(board)
##    MakeListOfFreeFields(board)
    EnterMove(board)

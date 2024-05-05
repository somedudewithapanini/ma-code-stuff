board=['-','-','-',
       '-','-','-',
       '-','-','-']
current_player='x'
winner=None
gamerunning=True



#make da board
def printboard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])    



#take input from player
def p_input(board):
    inp=int(input('enter a number 1-9 '))
    if inp>=1 and inp<=9 and board[inp-1]=='-':
        board[inp-1]=current_player
    else:
        print('uh-oh, the spot you want is alredy taken')

    
#check win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] ==board[2] and board[1] != '-':
        winner=board[0]
        return True
    elif board[3] == board[4] ==board[5] and board[5] != '-':
        winner=board[3]
        return True
    elif board[6] == board[7] ==board[8] and board[8] != '-':
        winner=board[8]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] ==board[6] and board[6] != '-':
        winner=board[0]
        return True
    elif board[1] == board[4] ==board[7] and board[1] != '-':
        winner=board[1]
        return True
    elif board[2] == board[5] ==board[8] and board[2] != '-':
        winner=board[2]
        return True
def check_diagonal(board):
    global winner
    if board[0] == board[4] ==board[8] and board[8] != '-':
        winner=board[0]
        return True
    elif board[2] == board[4] ==board[6] and board[2] != '-':
        winner=board[2]
        return True
def check_tie(board):
    global gamerunning
    if '-' not in board:
        printboard(board)
        print('tie game')
        gamerunning=False

def checkwin():
    global gamerunning
    if check_horizontal(board) or check_diagonal(board) or check_vertical(board):
        print(f'the winner is {winner}')
        gamerunning=False

#switch player
def switchplayer():
    global current_player
    if current_player == 'x':
        current_player='O'
    else:
        current_player='x'
#check win or tie... again

while gamerunning:
    printboard(board)
    p_input(board)
    checkwin()
    check_tie(board)
    switchplayer()
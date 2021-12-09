# board={
# 'tL':'','tM':'','tR':'',
# 'mL':'','mM':'','mR':'',
# 'lL':'','lM':'','lR':''}
board=[['*','*',''],['4','3','6'],['0','0','0']]

# def showBoard(board):
#     print(f"\n{board['tL']} | {board['tM']} | {board['tR']}   123")
#     print('-+--+-')
#     print(f"{board['mL']} | {board['mM']} | {board['mR']}   456")
#     print('-+--+-')
#     print(f"{board['lL']} | {board['lM']} | {board['lR']}   789\n")

def newGame(board):
    print("Welcome to tic tac toe * represents empty. \n")
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            board[i][j]='*'

def showBoard(board):
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            print(f"\t| {board[i][j]} | ",end="")
        print('')

newGame(board)
while True:
    showBoard(board)
    print('')
    inp=input('enter X in (i,j with comma): (leave blank to exit) ')
    if(inp==''):
        break
    pos=inp.split(',')
    posI=int(pos[0])
    posJ=int(pos[1])
    # print(pos)
    board[posI][posJ]='X'
    # showBoard(board)

   
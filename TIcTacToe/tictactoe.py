'''
Brandon Ellis
CSE210 TicTacToe
01/10/2022
First assignment for programming with functions
'''

def main():
    print("Welcome to Tic-Tac-Toe!\n[1] START GAME\n[2] EXIT\n")
    inCheck = True
    while inCheck:
        user_input = input("> ")
        if user_input == "1":
            inCheck = False
        elif user_input == "2":
            exit()
        else:
            inCheck = True
            print("Invalid response! Please enter a number choice...")

    player,gameBoard,is_winner = gameStart()

    while is_winner == False:
        gameBoard = playerTurn(player,gameBoard)
        is_winner, winner = validate(gameBoard)
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
    
    



def validate(game):
    cases = []
    A = []
    B = []
    C = []
    rd = [game[0][0],game[1][1],game[2][2]]
    ld = [game[0][2],game[1][1],game[2][0]]
    for i in game:
        cases.append(i)
        A.append(i[0])
        B.append(i[1])
        C.append(i[2])
    cases.extend((A,B,C,ld,rd))
    for i in cases:
        if all(v == 1 for v in i):
            return True, 1
        elif all(v == 2 for v in i):
            return True, 2
    return False, 0
    

def playerTurn(player, game):
    print("\n")
    drawBoard(game)
    print("\nPLAYER ",player," TURN")

    inCheck = True
    while inCheck:
        move = input("Enter the coordinate for your next move (eg. \"A1\"):\n> ")
        if move[0] in ["A","B","C"] and move[1] in ["1","2","3"]:
            row = int(move[1])-1
            col = 0
            if move[0] == "A":
                col = 0
            elif move[0] == "B":
                col = 1
            else:
                col = 2

            if game[row][col] == 0:
                inCheck = False
            else:
                print("Coordinate already occupied")

        else:
            print("Invalid Coordinate")
    
    

    game[row][col] = player
    return game


def gameStart():
    return 1, [[0,0,0],[0,0,0],[0,0,0]],False

def drawBoard(game):
    def drawRow(row,rowNum):
        rowValues = []
        for i in row:
            value = " "
            if i == 1:
                value = "X"
            elif i == 2:
                value = "O"
            rowValues.append(value)
        print(rowNum," ",rowValues[0]," | ",rowValues[1]," | ",rowValues[2])
    spacer = "   "+"-"*16
    print("    A     B     C ")
    drawRow(game[0],1)
    print(spacer)
    drawRow(game[1],2)
    print(spacer)
    drawRow(game[2],3)
    
if __name__ == "__main__":
    main()





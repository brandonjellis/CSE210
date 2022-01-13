'''
Brandon Ellis
CSE210 TicTacToe
01/10/2022
First assignment for programming with functions
'''

from random import randint as r

def main():
    score = [0,0]
    gameLoop = True

    
    print("Welcome to Tic-Tac-Toe!\n[1] START GAME\n[2] EXIT\n")
    inCheck = True
    while inCheck:
        user_input = input("> ")
        if user_input == "1":
            inCheck = False
        elif user_input == "2":
            print("Thank you for playing!")
            exit()
        else:
            inCheck = True
            print("Invalid response! Please enter a number choice...")

    while gameLoop:
        player,gameBoard,is_winner = gameStart()

        while is_winner == False:
            gameBoard = playerTurn(player,gameBoard)
            is_winner, winner = validate(gameBoard)
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
        
        print("\n")
        drawBoard(gameBoard)
        score = gameWinner(winner,score)

        print("\nPlay again?\n[1] YES\n[2] NO\n")
        inCheck = True
        while inCheck:
            user_input = input("> ")
            if user_input == "1":
                inCheck = False 
            elif user_input == "2":
                gameLoop = False
                inCheck =  False
            else:
                inCheck = True
                print("Invalid response! Please enter a number choice...")

    print("Thank you for playing!")
    exit()
    
    



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
    if all(0 not in l for l in cases):
        return True, 3
    else:
        return False, 0
    

def playerTurn(player, game):
    print("\n")
    drawBoard(game)
    print("\nPLAYER ",player," TURN")

    inCheck = True
    while inCheck:
        move = input("Enter the coordinate for your next move (eg. \"A1\"):\n> ")
        move = move.strip()
        move = move.upper()
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

def gameWinner(winner,score):
    if winner == 3:
        print("\nIt's a draw!")
    else:
        print("\nPlayer ",winner," wins!")
        score[winner-1] += 1
        print("The score is...\nX:",score[0],"\nO:",score[1])

    return score

def gameStart():
    player = r(1,2)
    print("A coin is flipped... Player ",player," will go first!")

    return player, [[0,0,0],[0,0,0],[0,0,0]],False

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





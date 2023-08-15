from random import randrange

def DisplayBoard(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for cell in row:
            print("|   " + str(cell) + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def EnterMove(board):
    while True:
        move = input("Ingresa tu movimiento: ")
        if move in ['1','2','3','4','5','6','7','8','9']:
            move = int(move)
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("El cuadro ya está ocupado, elige otro.")
        else:
            print("Entrada no válida. Ingresa un número entre 1 y 9.")

def MakeListOfFreeFields(board):
    freeFields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                freeFields.append((i, j))
    return freeFields

def VictoryFor(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign: return True
        if board[0][i] == board[1][i] == board[2][i] == sign: return True
    if board[0][0] == board[1][1] == board[2][2] == sign: return True
    if board[0][2] == board[1][1] == board[2][0] == sign: return True
    return False

def DrawMove(board):
    freeMoves = MakeListOfFreeFields(board)
    if len(freeMoves) == 0: return
    move = freeMoves[randrange(len(freeMoves))]
    board[move[0]][move[1]] = 'X'

# Iniciar el juego
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
while True:
    DisplayBoard(board)
    if len(MakeListOfFreeFields(board)) == 0 or VictoryFor(board, 'O') or VictoryFor(board, 'X'):
        break
    EnterMove(board)
    if len(MakeListOfFreeFields(board)) == 0 or VictoryFor(board, 'O'):
        break
    DrawMove(board)

DisplayBoard(board)
if VictoryFor(board, 'O'):
    print("¡Has Ganado!")
elif VictoryFor(board, 'X'):
    print("¡La máquina ha ganado!")
else:
    print("¡Es un empate!")

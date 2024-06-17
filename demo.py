import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def make_move(self, board, row, col, value):
        if is_valid(board, value, (row, col)):
            board[row][col] = value
            self.score += 1
            return True
        return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid(board, num, pos):
 
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

  
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

  
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    find = find_empty(board)
    if find[0] is None:
        return True

    row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)

   
    for _ in range(40):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0

    return board

def play_game(players):
    board = generate_board()
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

    while empty_cells:
        for player in players:
            print_board(board)
            print(f"{player.name}'s turn. Score: {player.score}")

            row, col = random.choice(empty_cells)
            print(f"Suggested move: row={row+1}, col={col+1}")
            value = int(input(f"{player.name}, enter a value (1-9): "))

            if player.make_move(board, row, col, value):
                empty_cells.remove((row, col))
            else:
                print("Invalid move. Try again.")

    print("Game over!")
    for player in players:
        print(f"{player.name}'s final score: {player.score}")


player1 = Player("Player 1")
player2 = Player("Player 2")
play_game([player1, player2])

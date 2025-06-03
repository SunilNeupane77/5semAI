# Write program to implement Tic Tac Toe game using recursion
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe(board, current_player):
    print_board(board)
    if check_winner(board, "X"):
        print("Player X wins!")
        return
    if check_winner(board, "O"):
        print("Player O wins!")
        return
    if is_full(board):
        print("It's a draw!")
        return

    print(f"Player {current_player}'s turn.")
    try:
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
    except ValueError:
        print("Please enter valid numbers.")
        tic_tac_toe(board, current_player)
        return

    if row not in range(3) or col not in range(3):
        print("Invalid move. Try again.")
        tic_tac_toe(board, current_player)
        return
    if board[row][col] != " ":
        print("Cell already taken. Try again.")
        tic_tac_toe(board, current_player)
        return

    board[row][col] = current_player
    next_player = "O" if current_player == "X" else "X"
    tic_tac_toe(board, next_player)

if __name__ == "__main__":
    board = [[" " for _ in range(3)] for _ in range(3)]
    tic_tac_toe(board, "X")
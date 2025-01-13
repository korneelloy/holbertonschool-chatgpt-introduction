#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the game board.

    Args:
        board (list): A 2D list representing the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner in the game.

    Args:
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Check if the game board is full.

    Args:
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play a game of Tic Tac Toe.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize the game board
    player = "X"  # Start with player X

    while True:
        print_board(board)

        # Prompt the current player for their move
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Check for valid input
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter a number between 0 and 2.")
                continue

            # Check if the chosen cell is empty
            if board[row][col] == " ":
                board[row][col] = player
                # Check for a winner
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                # Check for a tie
                if is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                # Switch to the other player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter numeric values for row and column.")
        except IndexError:
            print("Invalid input! Please enter a number between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()

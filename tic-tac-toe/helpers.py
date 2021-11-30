def display_board(board):
    print("\n" * 100)

    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")


def check_win(board, marker):
    """Checks to see if player won

    Args:
        board: current game board
        marker (int): current user marker
    """
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or  # across the top
            # across the middle
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            # across the bottom
            (board[1] == marker and board[2] == marker and board[3] == marker) or
            # down the left side
            (board[7] == marker and board[4] == marker and board[1] == marker) or
            # down the middle
            (board[8] == marker and board[5] == marker and board[2] == marker) or
            # down the right side
            (board[9] == marker and board[6] == marker and board[3] == marker) or
            # diagonal
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            # diagonal
            (board[3] == marker and board[5] == marker and board[7] == marker))

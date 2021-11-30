import random


def choose_first():
    """Check which player goes first

    Returns:
        str: Which player goes first (player 1 or player 2)
    """
    first_player = random.randint(0, 1)

    if first_player == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == " "


def player_input():
    """Takes user input from player to assign either X or O marker to that player

    Returns:
        tuple: includes both players respective markers
    """

    player_marker = ""

    while not (player_marker == "X" or player_marker == "O"):
        player_marker = input(
            "Player 1: Do you want to be X or O? ").upper()

        if not (player_marker == "X" or player_marker == "O"):
            print("Wrong Input! Please chose between X or O")

    if player_marker == "X":
        return ("X", "O")
    elif player_marker == "O":
        return ("O", "X")


def place_marker(board, marker, position):
    """Updates game board with user input

    Args:
        board (list): includes all values for each board place
        marker: X or O
        position (int): number between 1-9
    """
    board[position] = marker


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board, player, marker):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(
            input(f"{player} ({marker}), choose your next position: (1-9) "))

    return position


def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")

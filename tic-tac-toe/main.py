# Python TIC TAC TOE GAME

# Imports
from logo_art import logo_art
from helpers import display_board, check_win
from functions import *

game_over = False


# Game Script
print(logo_art)
print("Welcome to Tic Tac Toe")

while not game_over:
    game_board = [" "] * 10
    player_one_marker, player_two_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = input("Are you ready to play? Enter Yes or No. ")

    if play_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            # Player 1 turn
            display_board(game_board)
            position = player_choice(game_board, "Player 1", player_one_marker)
            place_marker(game_board, player_one_marker, position)

            if check_win(game_board, player_one_marker):
                display_board(game_board)
                print("Congratulations! Player 1, You've won the game!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = " Player 2"

        else:
            # Player 2 turn
            display_board(game_board)
            position = player_choice(game_board, "Player 2", player_two_marker)
            place_marker(game_board, player_two_marker, position)

            if check_win(game_board, player_two_marker):
                display_board(game_board)
                print("Congratulations! Player 2, You've won the game!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break

def create_game_board(values):
    print("\n")
    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}     ".format(values[0], values[1], values[2], values[3]))
    print('\t_____|_____|_____|_____')

    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}     ".format(values[4], values[5], values[6], values[7]))
    print('\t_____|_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}  |  {}     ".format(values[8], values[9], values[10], values[11]))
    print('\t_____|_____|_____|_____')

    print("\t     |     |     |")

    print("\t  {}  |  {}  |  {}  |  {}     ".format(values[12], values[13], values[14], values[15]))
    print("\t     |     |     |")

    print("\n")


def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t       	   SCOREBOARD       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")


def check_win(player_position, current_player):
    sol = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
           [4, 8, 12, 16], [1, 6, 11, 16], [4, 7, 10, 13]]
    for x in sol:
        if all(y in player_position[current_player] for y in x):
            return True
    return False


def check_draw(player_position):
    if len(player_position['A']) + len(player_position['B']) + len(player_position['C']) + len(
            player_position['D']) == 16:
        return True
    return False


def make_move(current_player):
    values = [' ' for i in range(16)]
    player_position = {'A': [], 'B': [], 'C': [], 'D': []}

    while True:
        create_game_board(values)

        try:
            print("Player ", current_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        if move < 1 or move > 16:
            print("Wrong Input!!! Try Again")
            continue

        if values[move - 1] != ' ':
            print("Place already filled. Try again!!")
            continue

        # Update game information
        # Updating grid status
        values[move - 1] = current_player

        # Updating player positions
        player_position[current_player].append(move)

        if check_win(player_position, current_player):
            create_game_board(values)
            print("Player ", current_player, " has won the game!!")
            print("\n")
            return current_player

        if check_draw(player_position):
            create_game_board(values)
            print("Game Drawn")
            print("\n")
            return 'L'


if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")

    current_player_1 = player1
    current_player_2 = player2
    # Stores the choice of players
    player_choice = {'A': "", 'B': "", 'C': "", 'D': ""}
    # Stores the options
    options = ['A', 'B', 'C', 'D']
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    while True:

        print("Turn to choose for", current_player_1)
        print("Enter 1-A, 2-B, 3-C, 4-D")
        print("Enter 5 to Quit")
        try:
            choice_1 = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        if choice_1 == 1:
            player_choice['A'] = current_player_1
        elif choice_1 == 2:
            player_choice['B'] = current_player_1
        elif choice_1 == 3:
            player_choice['C'] = current_player_1
        elif choice_1 == 4:
            player_choice['D'] = current_player_1
        elif choice_1 == 5:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        print("Turn to choose for", current_player_2)
        print("Enter 1-A, 2-B, 3-C, 4-D")
        print("Enter 5 to Quit")
        try:
            choice_2 = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
        if choice_2 == 1:
            player_choice['A'] = current_player_2
        elif choice_2 == 2:
            player_choice['B'] = current_player_2
        elif choice_2 == 3:
            player_choice['C'] = current_player_2
        elif choice_2 == 4:
            player_choice['D'] = current_player_2
        elif choice_2 == 5:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        winner_1 = make_move(options[choice_1 - 1])
        winner_2 = make_move(options[choice_2 - 1])

        # Edits the scoreboard according to the winner
        if winner_1 != 'L' and winner_2 != 'L':
            player_won = player_choice[winner_1] or player_choice[winner_2]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)

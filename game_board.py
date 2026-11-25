import random

# board structure

def create_board():

    return [[[" "] * 4 for _ in range(4)] for _ in range(4)]
    # i and j deleted for not use #


def show_board(board):
    for i in range(4):
        print("    Layer", i, end="                 ")

    print()

    for i in range(4):
        for j in range(4):
            print(board[j][i], end="       ")
        print()

# game functions

def generate_winning_lines():

    lines = []

    for i in range(4):

        for j in range(4):

            # Horizontal
            lines.append([(i, j, k) for k in range(4)])

            # Vertical
            lines.append([(i, k, j) for k in range(4)])

            # Across layers
            lines.append([(k, i, j) for k in range(4)])

        # Diagonals inside layers
        lines.append([(i, k, k) for k in range(4)])
        lines.append([(i, k, 3-k) for k in range(4)])

        # Diagonals across layers
        lines.append([(k, i, k) for k in range(4)])
        lines.append([(k, i, 3-k) for k in range(4)])

        lines.append([(k, k, i) for k in range(4)])
        lines.append([(k, 3-k, i) for k in range(4)])

    # 3D Diagonals
    lines.append([(k, k, k) for k in range(4)])
    lines.append([(k, k, 3-k) for k in range(4)])
    lines.append([(k, 3-k, k) for k in range(4)])
    lines.append([(k, 3-k, 3-k) for k in range(4)])

    return lines

winning_lines = generate_winning_lines()


def check_win(board, player):

    for line in winning_lines:

        count = 0

        for layer, row, col in line:

            if board[layer][row][col] == player:

                count += 1

        if count == 4:

            return True

    return False

def get_winner(board):

    if check_win(board, "x"):
        return "x"

    if check_win(board, "o"):
        return "o"

    return None

def get_available_moves(board):

    available_moves = []

    for layer in range(4):
        for row in range(4):
            for col in range(4):
                if board[layer][row][col] == " ":
                    available_moves.append((layer, row, col))

    return available_moves


def is_valid_move(board, layer, row, col):

    if 0 <= layer < 4 and 0 <= row < 4 and 0 <= col < 4:

        return board[layer][row][col] == " "        #  true or flase

    return False

def make_move(board, layer, row, col, player):

    if player not in ["x", "o"]:
        return False

    if is_valid_move(board, layer, row, col):

        board[layer][row][col] = player

        return True

    return False

def undo_move(board, layer, row, col):

    board[layer][row][col] = " "

def check_draw(board):

    return len(get_available_moves(board)) == 0 and get_winner(board) is None


def is_terminal(board):

    return get_winner(board) is not None or len(get_available_moves(board)) == 0


def switch_player(player):

    if player == "x":
        return "o"

    return "x"

# game inputs

def play_game():

    board = create_board()

    show_board(board)

    human_choice = input("\nChoose x or o: ").lower()

    while human_choice not in ["x", "o"]:

        print("Invalid choice! Try again")
        human_choice = input("Choose x or o: ").lower()

    ai_choice = switch_player(human_choice)

    while True:

        valid_human_choose = False

        while not valid_human_choose:

            try:

                chosen_board = int(input("Choose a board (from 0 to 3): "))
                chosen_row = int(input("Choose a row (from 0 to 3): "))
                chosen_column = int(input("Choose a column (from 0 to 3): "))

            except ValueError:

                print("Please enter integers only!")
                continue

            if make_move(board, chosen_board, chosen_row, chosen_column, human_choice):

                valid_human_choose = True

            else:
                print("Invalid move! Try again.")

        print("\nHuman move:")
        show_board(board)

        if is_terminal(board):
            break

        ai_board, ai_row, ai_column = random.choice(get_available_moves(board))

        make_move(board, ai_board, ai_row, ai_column, ai_choice)

        print("\nAI move:")
        show_board(board)

        if is_terminal(board):
            break

    winner = get_winner(board)

    if winner == human_choice:
        print("Human wins!")

    elif winner == ai_choice:
        print("AI wins!")

    else:
        print("Draw!")

if __name__ == "__main__":
    play_game()






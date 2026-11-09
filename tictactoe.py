import random


board = [" " for i in range(9)]


def print_board():
    print()
    for i in range(3):
        row = ""
        for j in range(3):
            row = row + " " + board[i * 3 + j] + " "
            if j < 2:
                row = row + "|"
        print(row)
        if i < 2:
            print("---+---+---")
    print()


def check_winner(b, player):

    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combos:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False


def is_board_full(b):
    for spot in b:
        if spot == " ":
            return False
    return True


def empty_spots(b):
    spots = []
    for i in range(9):
        if b[i] == " ":
            spots.append(i)
    return spots


def minimax(b, is_maximizing, alpha, beta):

    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_board_full(b):
        return 0

    if is_maximizing:
        best_score = -100
        for i in empty_spots(b):
            b[i] = "O"
            score = minimax(b, False, alpha, beta)
            b[i] = " "
            if score > best_score:
                best_score = score

            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = 100
        for i in empty_spots(b):
            b[i] = "X"
            score = minimax(b, True, alpha, beta)
            b[i] = " "
            if score < best_score:
                best_score = score
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score


def ai_move(difficulty):

    if difficulty == "easy" and random.random() < 0.4:
        move = random.choice(empty_spots(board))
        board[move] = "O"
        return

    if difficulty == "medium" and random.random() < 0.2:
        move = random.choice(empty_spots(board))
        board[move] = "O"
        return

    best_score = -100
    best_move = -1
    for i in empty_spots(board):
        board[i] = "O"
        score = minimax(board, False, -100, 100)
        board[i] = " "
        if score > best_score:
            best_score = score
            best_move = i

    board[best_move] = "O"


def human_move():
    while True:
        try:
            move = int(input("Pick a spot (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9!")
            elif board[move] != " ":
                print("That spot is taken! Try again.")
            else:
                board[move] = "X"
                break
        except ValueError:
            print("Thats not a valid number! Try again.")


def play_game():
    global board
    board = [" " for i in range(9)]  # reset board

    print("=== TIC TAC TOE ===")
    print("You are X, Computer is O")
    print()
    print("The board positions are:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    print("Choose difficulty:")
    print("1 - Easy   (AI makes random moves sometimes)")
    print("2 - Medium (AI is decent)")
    print("3 - Hard   (AI plays perfectly, good luck!)")
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice in ["1", "2", "3"]:
            break
        print("Invalid choice!")

    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    else:
        difficulty = "hard"

    print("\nLet's go! You move first.\n")


    while True:

        print_board()
        human_move()


        if check_winner(board, "X"):
            print_board()
            print("You win!! Nice job!")
            break

        if is_board_full(board):
            print_board()
            print("It's a tie!")
            break

        print("Computer is thinking...")
        ai_move(difficulty)


        if check_winner(board, "O"):
            print_board()
            print("Computer wins! Better luck next time.")
            break


        if is_board_full(board):
            print_board()
            print("It's a tie!")
            break

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ")
        if again.lower() != "y":
            print("Thanks for playing!")
            break

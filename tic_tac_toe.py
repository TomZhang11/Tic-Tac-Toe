import random


def initialize():
    diff = ""
    size_of_board = input("enter the size of the board: (int >= 3) ")
    while (
        not size_of_board.isdigit()
        or int(size_of_board) < 3
        or int(size_of_board) % 1 != 0
    ):
        size_of_board = input("enter a valid size: ")
    size_of_board = int(size_of_board)
    board = []
    for i in range(size_of_board):
        board.append([])
        for j in range(size_of_board):
            board[i].append(" ")
    computer = input("do you want to play with a computer? (yes, no) ")
    while computer != "yes" and computer != "no":
        computer = input("enter a valid answer: ")
    if computer == "yes":
        diff = input(
            "do you want to play with an easy, normal, or impossible computer: (easy, normal, impossible) "
        )
        while diff != "easy" and diff != "normal" and diff != "impossible":
            diff = input("enter a valid difficulty: ")
    return (
        size_of_board,
        board,
        computer,
        "x",
        0,
        size_of_board * size_of_board,
        diff,
        0,
        0,
    )


def play_again(string):
    again = input(string + ", play again? (yes, no) ")
    while again != "yes" and again != "no":
        again = input("please enter a valid answer: ")
    return again


def check_row(board, size_of_board, y, x, y1, x1):
    row_x = 0
    row_o = 0
    column_x = 0
    column_o = 0
    decline_x = 0
    decline_o = 0
    incline_x = 0
    incline_o = 0
    for i in range(size_of_board):
        if board[y][i] != "x":
            row_x += 1
        if board[i][x] != "x":
            column_x += 1
        if board[i][i] != "x":
            decline_x += 1
        if board[-i - 1][i] != "x":
            incline_x += 1
        if board[y1][i] != "o":
            row_o += 1
        if board[i][x1] != "o":
            column_o += 1
        if board[i][i] != "o":
            decline_o += 1
        if board[-i - 1][i] != "o":
            incline_o += 1
    if row_o == 1:
        for i in range(size_of_board):
            if board[y1][i] == " ":
                return y1, i
    if column_o == 1:
        for i in range(size_of_board):
            if board[i][x1] == " ":
                return i, x1
    if decline_o == 1:
        for i in range(size_of_board):
            if board[i][i] == " ":
                return i, i
    if incline_o == 1:
        for i in range(size_of_board):
            if board[-i - 1][i] == " ":
                return -i - 1, i
    if row_x == 1:
        for i in range(size_of_board):
            if board[y][i] == " ":
                return y, i
    if column_x == 1:
        for i in range(size_of_board):
            if board[i][x] == " ":
                return i, x
    if decline_x == 1:
        for i in range(size_of_board):
            if board[i][i] == " ":
                return i, i
    if incline_x == 1:
        for i in range(size_of_board):
            if board[-i - 1][i] == " ":
                return -i - 1, i
    return y, x


def check_win(board, y, x, player):
    if player == "computer":
        player = "o"
    horizontal_win = True
    vertical_win = True
    incline_win = True
    decline_win = True
    for i in range(size_of_board):
        if board[y][i] != player:
            horizontal_win = False
        if board[i][x] != player:
            vertical_win = False
        if board[i][i] != player:
            decline_win = False
        if board[-i - 1][i] != player:
            incline_win = False
    return horizontal_win or vertical_win or incline_win or decline_win


def play_ahead(board, y, x, player, count, empty_spots):
    if check_win(board, y, x, player):
        if player == "o":
            return 1, 1
        else:
            return -1, -1
    elif count == max_moves:
        return 0, 0
    else:
        if player == "o":
            player = "x"
        else:
            player = "o"
        l = []
        j = 0
        li = []
        for i in empty_spots:
            y = i // size_of_board
            x = i % size_of_board
            board[y][x] = player
            empty_spots.remove(i)
            a, b = play_ahead(board, y, x, player, count + 1, empty_spots)
            li.append(b)
            board[y][x] = " "
            empty_spots.insert(j, i)
            l.append(a)
            j += 1
        if board == orig_board:
            mxP = -80000
            mx = max(l)
            ideal_spot = 0
            for i in range(len(l)):
                if l[i] == mx:
                    if li[i] > mxP:
                        ideal_spot = empty_spots[i]
                        mxP = li[i]
            # print(empty_spots)
            # print(l)
            # print(li)
            return ideal_spot // size_of_board, ideal_spot % size_of_board
        else:
            if player == "o":
                return max(l), sum(li)
            else:
                return min(l), sum(li)


size_of_board, board, computer, player, count, max_moves, diff, y1, x1 = initialize()

while True:
    count += 1
    # turn
    print(player + "'s turn")
    if player != "computer":
        x = input("enter an x coordinate: (1 to %s) " % size_of_board)
        while x.isdigit() == False or int(x) < 1 or int(x) > size_of_board:
            x = input("enter a valid coordinate: ")
        y = input("enter an y coordinate: (1 to %s) " % size_of_board)
        while y.isdigit() == False or int(y) < 1 or int(y) > size_of_board:
            y = input("enter a valid coordinate: ")
        x = int(x) - 1
        y = int(y) - 1
        while not board[y][x] == " ":
            x = input("enter a valid x coordinate: ")
            while x.isdigit() == False or int(x) < 1 or int(x) > 3:
                x = input("enter a valid coordinate: ")
            y = input("enter a valid y coordinate: ")
            while y.isdigit() == False or int(y) < 1 or int(y) > 3:
                y = input("enter a valid coordinate: ")
            x = int(x) - 1
            y = int(y) - 1
        board[y][x] = player
    else:
        # computer turn
        if diff == "easy":
            while board[y][x] != " ":
                y = random.randint(0, size_of_board - 1)
                x = random.randint(0, size_of_board - 1)
        elif diff == "normal":
            y, x = check_row(board, size_of_board, y, x, y1, x1)
            if board[y][x] != " ":
                while board[y][x] != " ":
                    y = random.randint(0, size_of_board - 1)
                    x = random.randint(0, size_of_board - 1)
        else:
            y, x = check_row(board, size_of_board, y, x, y1, x1)
            if board[y][x] != " ":
                orig_board = []
                for i in board:
                    orig_board.append(i.copy())
                empty_spots = []
                for i in range(size_of_board):
                    for j in range(size_of_board):
                        if board[i][j] == " ":
                            empty_spots.append(i * 3 + j)
                mid = len(board) // 2
                if board[mid][mid] == " ":
                    y, x = (mid, mid)
                else:
                    y, x = play_ahead(board, y, x, "x", count, empty_spots)
        y1 = y
        x1 = x
        board[y][x] = "o"
    # print board
    for i in range(size_of_board):
        print(board[i])
    # check_win
    if check_win(board, y, x, player):
        again = play_again(player + " wins")
        if again == "yes":
            (
                size_of_board,
                board,
                computer,
                player,
                count,
                max_moves,
                diff,
                y1,
                x1,
            ) = initialize()
            continue
        else:
            break
    # check draw
    if count == max_moves:
        again = play_again("draw")
        if again == "yes":
            (
                size_of_board,
                board,
                computer,
                player,
                count,
                max_moves,
                diff,
                y1,
                x1,
            ) = initialize()
            continue
        else:
            break
    # player switch
    if player == "x":
        if computer == "no":
            player = "o"
        else:
            player = "computer"
    else:
        player = "x"
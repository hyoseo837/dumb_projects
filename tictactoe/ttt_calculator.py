
def check_win(board):
    for j in [0,3,6]:
        if board[j] == board[j+1] and board[j] == board[j+2] and board[j] != "-":
            return board[j]
    for j in [0,1,2]:
        if board[j] == board[j+3] and board[j] == board[j+6] and board[j] != "-":
            return board[j]
    if board[0] == board[4] and board[0] == board[8] and board[0] != "-":
        return board[0]
    if board[2] == board[4] and board[2] == board[6] and board[2] != "-":
        return board[2]
    return "draw"


def calculate(stones):
    table = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    pl_1 = [stones[0],stones[2],stones[4],stones[6],stones[8]]
    for j in range(9):
        k = stones[j]
        if k in pl_1:
            table[k-1] = "1"
        else:
            table[k-1] = "2"
        result = check_win(table)
        if result == "1":
            return "player 1"
        elif result == "2":
            return "player 2"
        else:
            pass
    return "draw"

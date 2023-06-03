import ttt_calculator
import ttt_ai_algo
import os

# tic-tac-toe
choices = [1,2,3,4,5,6,7,8,9]
table = ["-","-","-","-","-","-","-","-","-"]
sign = ["o","x"]
turn = 1
log = []
loc = os.path.dirname(os.path.abspath(__file__))

def prt():
    print(f'''-------------------------------------

    {table[0]} | {table[1]} | {table[2]}
    ----------
    {table[3]} | {table[4]} | {table[5]}
    ----------
    {table[6]} | {table[7]} | {table[8]}
    ''')
    return

def human_player(turn):
    while True:
        choice = int(input(f"player {turn} : "))
        if choice in choices:
            if table[choice-1] == "-":
                return choice
        else:
            print("you can't put there")

def computer_player(turn):
    f = open(f"{loc}/ttt_data.txt", "r")
    contents = f.readlines()
    f.close()
    tat = []
    for i in contents:
        tat.append(i.split("::"))
    
    for i in tat:
        if str(log) == i[0]:
            choice = int(i[1][:-1])
            return choice
    choice = ttt_ai_algo.find_ans(log,turn)
    f = open(f"{loc}/ttt_data.txt", "a")
    f.write(f"{str(log)}::{choice}\n")
    f.close()
    return choice
    

prt()
for i in range(9):
    turn = (turn + 1) % 2
    if turn == 1:
        choice = human_player(1)
    elif turn == 0:
        choice = computer_player(0)
    table[choice-1] = sign[turn]
    log.append(choice)

    prt()

    end = ttt_calculator.check_win(table)
    if end == "draw":
        pass
    elif end == "x":
        print("player 1 win!")
        break
    elif end == "o":
        print("player 2 win!")
        break
if end == "draw":
    print("draw")

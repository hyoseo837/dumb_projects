
# tic-tac-toe
a = ["-","-","-","-","-","-","-","-","-"]
sign = ["o","x"]
turn = 1

def prt():
    print(f'''
    {a[0]} | {a[1]} | {a[2]}
    ----------
    {a[3]} | {a[4]} | {a[5]}
    ----------
    {a[6]} | {a[7]} | {a[8]}''')
    return

def check_win():
    for j in [0,3,6]:
        if a[j] == a[j+1] and a[j] == a[j+2] and a[j] != "-":
            print(f"==============\n{a[j]} won!\n=============")
            return False
    for j in [0,1,2]:
        if a[j] == a[j+3] and a[j] == a[j+6] and a[j] != "-":
            print(f"==============\n{a[j]} won!\n=============")
            return False
    if a[0] == a[4] and a[0] == a[8] and a[0] != "-":
        print(f"==============\n{a[0]} won!\n=============")
        return False
    if a[2] == a[4] and a[2] == a[6] and a[2] != "-":
        print(f"==============\n{a[0]} won!\n=============")
        return False
    return True


for i in range(0,9):
    prt()
    if check_win() is False:
        break

    turn = (turn + 1) % 2
    while True:
        choice = int(input(f"player {turn+1} : "))
        if a[choice-1] == "-":
            a[choice-1] = sign[turn]
            break
        else:
            print("again")

if check_win() is True:
    print("==============\ntie\n=============")
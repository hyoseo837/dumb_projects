import itertools
import random
import ttt_calculator


def find_ans(log,turn):
    INF = 10**10
    rates = []
    left = [1,2,3,4,5,6,7,8,9]
    for i in log:
        left.remove(i)

    left_clone = []
    for i in left:
        left_clone.append(i)

    for k in left_clone:
        t_logs = []
        left.remove(k)
        for i in itertools.permutations(left,len(left)):
            b = list(i)
            t_logs.append(log +[k]+ b)
            
        left = [1,2,3,4,5,6,7,8,9]
        for i in log:
            left.remove(i)
        
        count = 0
        wincount = 0
        losecount = 0
        for i in t_logs:
            count += 1
            result = ttt_calculator.calculate(i)
            if turn == 0:
                if result == "player 1":
                    losecount += 1
                if result == "player 2":
                    wincount += 1
            elif turn == 1:
                if result == "player 2":
                    losecount += 1
                if result == "player 1":
                    wincount += 1


        winrate = wincount/count
        loserate = losecount/count
        rates.append([k,winrate, loserate])

    g_lose = INF
    for i in rates:
        if i[2] < g_lose:
            decision = i[0]
            g_win = i[1]
            g_lose = i[2]
        elif i[2] == g_lose and i[1] > g_win:
            decision = i[0]
            g_win = i[1]
            g_lose = i[2]
        elif i[2] == g_lose and i[1] == g_win:
            if random.choice([True, False]):
                decision = i[0]
                g_win = i[1]
                g_lose = i[2]
                
        if i[1] >= 0.95:
            decision = i[0]
            g_win = i[1]
            g_lose = i[2]
            break

    return decision
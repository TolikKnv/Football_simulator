import json
from parts import *

score = [0,0]
ball = 1

# players = json.load(open("players.json"))
# print(players['goalkeepers']['Liam Smith'])
team_1 = None
team_2 = None
k = 0
num = 1
while k!=2:
    q = input(f'Введите имя вратаря для команды {num}: ')
    w = input(f'Введите имя защитника для команды {num}: ')
    e = input(f'Введите имя защитника для команды {num}: ')
    r = input(f'Введите имя защитника для команды {num}: ')
    t = input(f'Введите имя защитника для команды {num}: ')
    y = input(f'Введите имя полузащитника для команды {num}: ')
    u = input(f'Введите имя полузащитника для команды {num}: ')
    i = input(f'Введите имя полузащитника для команды {num}: ')
    o = input(f'Введите имя нападающего для команды {num}: ')
    p = input(f'Введите имя нападающего для команды {num}: ')
    a = input(f'Введите имя нападающего для команды {num}: ')
    if k==0:
        team_1 = team_gen(q, w, e, r, t, y, u, i, o, p, a)[1]
        team_1_stat = team_gen(q, w, e, r, t, y, u, i, o, p, a)[0]
        team_1[w]['status_ball'] = True
        k+=1
        num+=1
    else:
        team_2 = team_gen(q, w, e, r, t, y, u, i, o, p, a)[1]
        team_2_stat = team_gen(q, w, e, r, t, y, u, i, o, p, a)[0]
        k+=1

# buff(team_1_stat, team_2_stat, team_1, team_2)
# print(team_1)

s = 0
while s!=90:
    pass_ball(ball, team_1, team_2)
    shoot(ball, team_1, team_2, score)
    defence(ball, team_1, team_2)
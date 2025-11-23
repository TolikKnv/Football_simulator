import json
from random import randint, choice

players_only = json.load(open("players_only.json"))
players = json.load(open("players.json"))


def team_gen(q, w, e, r, t, y, u, i, o, p, a):
    attack = (
        players_only[q]["attack"]
        + players_only[w]["attack"]
        + players_only[e]["attack"]
        + players_only[r]["attack"]
        + players_only[t]["attack"]
        + players_only[y]["attack"]
        + players_only[u]["attack"]
        + players_only[i]["attack"]
        + players_only[o]["attack"]
        + players_only[p]["attack"]
        + players_only[a]["attack"]
    ) / 11
    defence = (
        players_only[q]["defence"]
        + players_only[w]["defence"]
        + players_only[e]["defence"]
        + players_only[r]["defence"]
        + players_only[t]["defence"]
        + players_only[y]["defence"]
        + players_only[u]["defence"]
        + players_only[i]["defence"]
        + players_only[o]["defence"]
        + players_only[p]["defence"]
        + players_only[a]["defence"]
    ) / 11
    technique = (
        players_only[q]["technique"]
        + players_only[w]["technique"]
        + players_only[e]["technique"]
        + players_only[r]["technique"]
        + players_only[t]["technique"]
        + players_only[y]["technique"]
        + players_only[u]["technique"]
        + players_only[i]["technique"]
        + players_only[o]["technique"]
        + players_only[p]["technique"]
        + players_only[a]["technique"]
    ) / 11
    total = (
        players_only[q]["total"]
        + players_only[w]["total"]
        + players_only[e]["total"]
        + players_only[r]["total"]
        + players_only[t]["total"]
        + players_only[y]["total"]
        + players_only[u]["total"]
        + players_only[i]["total"]
        + players_only[o]["total"]
        + players_only[p]["total"]
        + players_only[a]["total"]
    ) / 11
    ease_of_play = (
        (
            players_only[q]["ease_of_play"]
            + players_only[w]["ease_of_play"]
            + players_only[e]["ease_of_play"]
            + players_only[r]["ease_of_play"]
            + players_only[t]["ease_of_play"]
            + players_only[y]["ease_of_play"]
            + players_only[u]["ease_of_play"]
            + players_only[i]["ease_of_play"]
            + players_only[o]["ease_of_play"]
            + players_only[p]["ease_of_play"]
            + players_only[a]["ease_of_play"]
        )
        / 11,
    )
    return {
        "attack": attack,
        "defence": defence,
        "technique": technique,
        "total": total,
        "ease_of_play": ease_of_play,
    }, {
        f"{q}": players_only[q],
        f"{w}": players_only[w],
        f"{e}": players_only[e],
        f"{r}": players_only[r],
        f"{t}": players_only[t],
        f"{y}": players_only[y],
        f"{u}": players_only[u],
        f"{i}": players_only[i],
        f"{o}": players_only[o],
        f"{p}": players_only[p],
        f"{a}": players_only[a],
    }


def buff(team_1_stat, team_2_stat, team_1, team_2):
    if (
        team_1_stat["attack"] + team_1_stat["defence"] + team_1_stat["technique"]
        > team_2_stat["attack"] + team_2_stat["defence"] + team_2_stat["technique"]
    ):
        for item in team_1.values():
            item["attack"] *= 1.1
            item["defence"] *= 1.1
            item["technique"] *= 1.1
            print("Команда 1 фоварит")
    else:
        for item in team_2.values():
            item["attack"] *= 1.1
            item["defence"] *= 1.1
            item["technique"] *= 1.1
            print("Команда 2 фоварит")


def pass_ball(ball, team_1, team_2):
    a = randint(1, 100)
    now_ball_player = None
    if ball == 1 and a <= 50:
        for key in team_1.keys():
            if team_1[key]["status_ball"] == True:
                now_ball_player = key
        q = randint(1, 100)
        if (
            team_1[key] in list(players["attacking_midfielders"].keys())
            or team_1[key] in list(players["right_wings"].keys())
            or team_1[key] in list(players["left_wings"].keys())
            or team_1[key] in list(players["forwards"].keys())
        ) and q <= 20:
            flag = True
        elif not (
            team_1[key] in list(players["attacking_midfielders"].keys())
            or team_1[key] in list(players["right_wings"].keys())
            or team_1[key] in list(players["left_wings"].keys())
            or team_1[key] in list(players["forwards"].keys())
        ):
            flag = True
        else:
            flag = False
        while flag:
            ball_player = choice(list(team_1.keys()))
            if team_1[ball_player]["status_ball"] == True:
                continue
            else:
                team_1[ball_player]["status_ball"] = True
                team_1[now_ball_player]["status_ball"] = False
                flag = False
                print(
                    f"Команда 1 с мячом, игрок {now_ball_player} пасует игроку {ball_player}"
                )
    elif ball == 2 and a > 50:
        for key in team_2.keys():
            if team_2[key]["status_ball"] == True:
                now_ball_player = key
        flag = True
        while flag:
            ball_player = choice(list(team_2.keys()))
            if team_2[ball_player]["status_ball"] == True:
                continue
            else:
                team_2[ball_player]["status_ball"] = True
                team_2[now_ball_player]["status_ball"] = False
                flag = False
                print(
                    f"Команда 2 с мячом, игрок {now_ball_player} пасует игроку {ball_player}"
                )


def shoot(ball, team_1, team_2, score):
    a = randint(1, 100)
    now_ball_player = None
    flag = False
    if ball == 1 and a <= 50:
        goal_keeper = team_2[list(team_2.keys())[0]]
        for key in team_1.keys():
            if team_1[key]["status_ball"] == True and (
                key in players["attacking_midfielders"].keys()
                or key in players["right_wings"].keys()
                or key in players["left_wings"].keys()
                or key in players["forwards"].keys()
            ):
                now_ball_player = key
                flag = True
        if flag:
            print(f"Команда 1 с мячом, игрок {now_ball_player} бьет по воротам!")
            b = randint(1, 100)
            if b <= 80:
                print("Удар в створ!")
            else:
                print("Мимо!")
                return score
            c = randint(1, 100)
            if c <= 10:
                print("Гол! Такое не берётся!")
                score[0] += 1
                return score
            d = randint(1, 100)
            chance = (
                (
                    team_1[now_ball_player]["attack"]
                    + team_1[now_ball_player]["technique"]
                )
                / 2
                - goal_keeper["defence"]
                + 40
            )
            if d <= chance:
                print("Гол!")
                score[0] += 1
                return score
            else:
                print("Вратарь отбил!")
                return score
    elif ball == 2 and a > 50:
        goal_keeper = team_1[list(team_1.keys())[0]]
        for key in team_2.keys():
            if team_2[key]["status_ball"] == True and (
                key in players["attacking_midfielders"].keys()
                or key in players["right_wings"].keys()
                or key in players["left_wings"].keys()
                or key in players["forwards"].keys()
            ):
                now_ball_player = key
        if now_ball_player:
            print(f"Команда 1 с мячом, игрок {now_ball_player} бьет по воротам!")
            b = randint(1, 100)
            if b <= 80:
                print("Удар в створ!")
            else:
                print("Мимо!")
                return score
            c = randint(1, 100)
            if c <= 10:
                print("Гол! Такое не берётся!")
                score[1] += 1
                return score
            d = randint(1, 100)
            chance = (
                (
                    team_2[now_ball_player]["attack"]
                    + team_2[now_ball_player]["technique"]
                )
                / 2
                - goal_keeper["defence"]
                + 40
            )
            if d <= chance:
                print("Гол!")
                score[1] += 1
                return score
            else:
                print("Вратарь отбил!")
                return score

        # shot_chance = (
        #     team_1[now_ball_player]['attack']
        #     + team_1[now_ball_player]['technique']
        # ) / 2

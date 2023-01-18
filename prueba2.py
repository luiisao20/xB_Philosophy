import numpy as np
import pandas as pd

df = pd.read_csv("data_partida.csv", header=0)


def max_killer(kills, name):
    max_kill = max(kills)
    kill_arr = np.array(kills)
    a = list(np.where(kill_arr == max_kill))
    killers = []
    for b in range(len(a[0])):
        killers.append(name[a[0][b]])

    if len(killers) > 1:
        killers = ", ".join(killers)
        print("Los killers son {} con {} de kills cada uno".format(killers, max_kill))
    else:
        print("El MAXIMO killer es {} con {} kills".format(killers[0], max_kill))


def max_damages(damages, name):
    damage_max = max(damages)
    kill_arr = np.array(damages)
    a = list(np.where(kill_arr == damage_max))
    killers = []

    for b in range(len(a[0])):
        killers.append(name[a[0][b]])

    if len(killers) > 1:
        killers = ", ".join(killers)
        print("Los killers son {} con {} de daño cada uno".format(killers, damage_max))
    else:
        killer = name[damages.index(damage_max)]
        print("El MAXIMO killer es {} con {} de daño".format(killer, damage_max))


def max_assist(assists, name):
    assist_max = max(assists)
    kill_arr = np.array(assists)
    a = list(np.where(kill_arr == assist_max))
    killers = []

    for b in range(len(a[0])):
        killers.append(name[a[0][b]])

    if len(killers) > 1:
        killers = ", ".join(killers)
        print("Los asistidores son {} con {} asistencias cada uno".format(killers, assist_max))
    else:
        killer = name[assists.index(assist_max)]
        print("El MAXIMO asistidor es {} con {} asistencias".format(killer, assist_max))


def max_total_kills(teams, total_kills, damages):
    teams_new = []
    for a in range(48):
        if a % 4 == 0:
            teams_new.append(teams[a])
        else:
            pass

    print(teams_new)
    total_kills_n = []
    for b in range(48):
        if b % 4 == 0:
            total_kills_n.append(total_kills[b])
        else:
            pass
    print(total_kills_n)

    kills_max = max(total_kills_n)
    kill_arr = np.array(total_kills_n)
    a = list(np.where(kill_arr == kills_max))
    killers = []

    for b in range(len(a[0])):
        killers.append(teams_new[a[0][b]])

    if len(killers) > 1:
        killers = ", ".join(killers)
        print("Los asistidores son {} con {} asistencias cada uno".format(killers, kills_max))
    else:
        killer = teams_new[total_kills_n.index(kills_max)]
        print("El MAXIMO asistidor es {} con {} asistencias".format(killer, kills_max))

    #dano total
    e = 0
    f = 4
    damage_total = []
    for c in range(12):
        d = slice(e, f)
        damage_total.append(sum(damages[d]))
        e += 4
        f += 4
    print(damage_total)


def main():
    total_kills = list(df["killing_score"])
    teams = list(df["team_name"])
    assists = list(df["assists"])
    damages = list(df["damage"])
    name = list(df["nickname"])
    kills = list(df["kills"])

    max_killer(kills, name)
    max_damages(damages, name)
    max_assist(assists, name)
    max_total_kills(teams, total_kills, damages)


if __name__ == "__main__":
    main()

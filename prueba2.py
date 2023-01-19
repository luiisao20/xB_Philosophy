import heapq
import numpy as np
import pandas as pd

df = pd.read_csv("data_partida.csv", header=0)
name = list(df["nickname"])
teams = list(df["team_name"])


def maximum(items, word):

    object_sing = "content"
    if word == "kills":
        object_sing = "eliminaciones"
    elif word == "assists":
        object_sing = "asitencias"
    elif word == "damage":
        object_sing = "daño"
    elif word == "medkit":
        object_sing = "botiquines usados"
    elif word == "revived":
        object_sing = "compañeros revividos"
    elif word == "knock_down":
        object_sing = "derribos"
    elif word == "headshots":
        object_sing = "disparos a la cabeza"
    elif word == "grenade":
        object_sing = "granadas desplegadas"

    max_item = heapq.nlargest(3, zip(items, name))
    names = []
    kills = []
    index = 0
    for item in max_item:
        names.append(item[1])
        kills.append(item[0])
        index += 1

    print("Los 3 jugadores con mas {} son:\n"
          "{} con {} {}\n"
          "{} con {} {}\n"
          "{} con {} {}\n".format(object_sing, names[0], kills[0], object_sing,
                                  names[1], kills[1], object_sing,
                                  names[2], kills[2], object_sing))


def minimum(items):

    object_sing = "tiempo de supervivencia"

    # heapq.nlowest
    min_item = min(items)
    items_arr = np.array(items)
    a = list(np.where(items_arr == min_item))
    containers = []
    for b in range(len(a[0])):
        containers.append(name[a[0][b]])

    if len(containers) > 1:
        containers = ", ".join(containers)
        print("{} son los jugadores con menos {}, {} segundos cada uno.\n".format(containers, object_sing, min_item))
    else:
        print("{} es el jugador con menos {}, en total {} segundos .\n".format(containers[0], object_sing, min_item))


def get_one_item_for_teams(item):
    item_new = []
    for a in range(48):
        if a % 4 == 0:
            item_new.append(item[a])
        else:
            pass
    return item_new


def get_sum_item_for_teams(item):
    e = 0
    f = 4
    item_total = []
    for c in range(12):
        d = slice(e, f)
        item_total.append(sum(item[d]))
        e += 4
        f += 4
    return item_total


def maximum_for_teams(items, team_name, word):
    object_sing = "content"
    if word == "kills":
        object_sing = "eliminaciones"
    elif word == "assists":
        object_sing = "asitencias"
    elif word == "damage":
        object_sing = "daño"
    elif word == "medkit":
        object_sing = "botiquines usados"
    elif word == "revived":
        object_sing = "compañeros revividos"
    elif word == "knock_down":
        object_sing = "derribos"
    elif word == "headshots":
        object_sing = "disparos a la cabeza"
    elif word == "grenade":
        object_sing = "granadas desplegadas"

    max_item = heapq.nlargest(1, zip(items, team_name))

    print("{} es el equipo con mas {}, en total {}.".format(max_item[0][1], object_sing, max_item[0][0]))
    return max_item[0][0]


def max_total_kills(total_kills, damages):
    # Sacando una tabla de los 12 equipos
    teams_new = get_one_item_for_teams(teams)
    print(teams_new)

    # Sacando las kills totales por cada equipo
    total_kills_list = get_one_item_for_teams(total_kills)
    print(total_kills_list)

    # Obteniendo el equipo con más kills
    kills_total = maximum_for_teams(total_kills_list, teams_new, "kills")

    # Sacando el daño total por equipo
    damage_total_list = get_sum_item_for_teams(damages)
    print(damage_total_list)
    total_damage = maximum_for_teams(damage_total_list, teams_new, "damage")


def main():

    total_kills = list(df["killing_score"])
    assists = list(df["assists"])
    damages = list(df["damage"])
    kills = list(df["kills"])
    med_kit = list(df["medkit_use"])
    team_mates_revived = list(df["revive_teammate_times"])
    knock_down = list(df["knock_down"])
    headshots = list(df["headshots"])
    grenades = list(df["grenade_use"])
    survival_time = list(df["survival_time"])

    # Jugador con menos tiempo de supervivencia
    minimum(survival_time)
    # Jugador con mas granadas desplegadas
    maximum(grenades, "grenade")

    # Jugador con mas disparos a la cabeza
    maximum(headshots, "headshots")

    # Jugador con mas derribos
    maximum(knock_down, "knock_down")

    # Jugador que mas revivio
    maximum(team_mates_revived, "revived")

    # El jugador con mas botiquines usados
    maximum(med_kit, "medkit")

    # Sacando el jugador con más kills
    maximum(kills, "kills")

    # Sacando el jugador con más daño
    maximum(damages, "damage")

    # Sacando el jugador con más asistencias
    maximum(assists, "assists")

    # Sacando estadísticas de los equipos en conjunto
    max_total_kills(total_kills, damages)


if __name__ == "__main__":
    main()

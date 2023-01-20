import heapq
import numpy as np
import pandas as pd

df = pd.read_csv("data_partida.csv", header=0)
name = list(df["nickname"])
teams = list(df["team_name"])
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
booyah = list(df["booyah"])
score = list(df["ranking_score"])
revived_times = list(df["revived_times"])


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
    achievements = []
    index = 0
    for item in max_item:
        names.append(item[1])
        achievements.append(item[0])
        index += 1

    print("Los 3 jugadores con mas {} son:\n"
          "{} con {} {}\n"
          "{} con {} {}\n"
          "{} con {} {}\n".format(object_sing, names[0], achievements[0], object_sing,
                                  names[1], achievements[1], object_sing,
                                  names[2], achievements[2], object_sing))


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
    return max_item


def get_players_alive(survival_time_n):

    max_survival_time = max(survival_time_n[0])

    items_arr = np.array(survival_time_n[0])
    a = np.where(items_arr == max_survival_time)

    print("En el equipo de {}".format(survival_time_n[1]))

    if len(a[0]) == 4:
        print("Todos los jugadores quedaron vivos, el maximo tiempo de supervivencia fue {} segundos".format(max_survival_time))
        return 4, max_survival_time
    elif len(a[0]) == 3:
        print("3 jugadores quedaron vivos, el maximo tiempo de supervivencia fue {} segundos".format(max_survival_time))
        return 3, max_survival_time
    elif len(a[0]) == 2:
        print("2 jugadores quedaron vivos, el maximo tiempo de supervivencia fue {} segundos".format(max_survival_time))
        return 2, max_survival_time
    else:
        print("1 jugador quedo vivo, el maximo tiempo de supervivencia fue {} segundos".format(max_survival_time))
        return 1, max_survival_time


def get_statistics_for_best_teams(item, teams_new, positions, word):
    object_sing = "content"
    statistics_teams = item
    if word == "kills":
        object_sing = "ELIMINACIONES"
    elif word == "damage":
        object_sing = "DAÑOS"
    elif word == "damage":
        object_sing = "daño"
    elif word == "resurrects":
        object_sing = "RESURRECCIONES"
        statistics_teams = get_sum_item_for_teams(item)

    statistic_total_list = [[statistics_teams[teams_new.index(positions[0][1])], positions[0][1]],
                          [statistics_teams[teams_new.index(positions[1][1])], positions[1][1]],
                          [statistics_teams[teams_new.index(positions[2][1])], positions[2][1]]]
    print("{} DE LOS EQUIPOS ".format(object_sing), statistic_total_list)
    return statistic_total_list


def get_time_survival_and_survivors(teams_new, positions):
    e = 0
    f = 4
    survival_for_team = []
    for c in range(12):
        d = slice(e, f)
        survival_for_team.append(survival_time[d])
        e += 4
        f += 4

    players_alive_list = []
    max_survival_time_list = []

    for index in range(0, 3):
        survival_time_new = [survival_for_team[teams_new.index(positions[index][1])], positions[index][1]]
        players_alive, max_survival_time = get_players_alive(survival_time_new)
        players_alive_list.append(players_alive)
        max_survival_time_list.append(max_survival_time)

    print(players_alive_list, max_survival_time_list)
    return players_alive_list, max_survival_time_list


def xb_philosophy(score_list, teams_new, damage_total_list, total_kills_list):
    positions = heapq.nlargest(3, zip(score_list, teams_new))
    print("POSICIONES DE LOS EQUIPOS", positions)

    # Obteniendo las veces que usaron la resurreccion
    revived_total_list = get_statistics_for_best_teams(revived_times, teams_new, positions, "resurrects")

    damage_for_bests_teams = get_statistics_for_best_teams(damage_total_list, teams_new, positions, "damage")

    kills_for_bests_teams = get_statistics_for_best_teams(total_kills_list, teams_new, positions, "kills")

    num_players_alive, max_survival_time = get_time_survival_and_survivors(teams_new, positions)

    # Tiempo de supervivencia por equipo


def teams_statistics():
    # Sacando una tabla de los 12 equipos
    teams_new = get_one_item_for_teams(teams)

    # Sacando las kills totales por cada equipo
    total_kills_list = get_one_item_for_teams(total_kills)

    # Obteniendo el equipo con más kills
    kills_total = maximum_for_teams(total_kills_list, teams_new, "kills")

    # Obteniendo el equipo com mas daño
    damage_total_list = get_sum_item_for_teams(damages)
    total_damage = maximum_for_teams(damage_total_list, teams_new, "damage")

    # Sacando el daño total por equipo
    score_list = get_one_item_for_teams(score)
    # Daño máximo de partida
    highest_damages_teams = heapq.nlargest(3, zip(damage_total_list, teams_new))
    print("DAÑO MÁS ALTOS", highest_damages_teams)

    kills_for_bests_teams = heapq.nlargest(3, zip(total_kills_list, teams_new))

    print("EQUIPOS CON MÁS KILLS", kills_for_bests_teams)

    titulo = "EXPECTATIVE BOOYAH PHILOSOPHY"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    xb_philosophy(score_list, teams_new, damage_total_list, total_kills_list)


def main():
    titulo = "DATOS POR JUGADORES, ELIGIENDO LOS MEJORES 3"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

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

    titulo = "DATOS POR EQUIPOS"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    # Sacando estadísticas de los equipos en conjunto
    teams_statistics()


if __name__ == "__main__":
    main()

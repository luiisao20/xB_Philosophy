import heapq
import numpy as np
import pandas as pd


def get_one_item_for_teams(item):
    item_new = []
    for a in range(48):
        if a % 4 == 0:
            item_new.append(item[a])
        else:
            pass
    return item_new


def get_players_alive(survival_time_n):

    max_survival_time = max(survival_time_n[0])

    items_arr = np.array(survival_time_n[0])
    a = np.where(items_arr == max_survival_time)

    # print("En el equipo de {}".format(survival_time_n[1]))

    if len(a[0]) == 4:
        # print("Todos los jugadores quedaron vivos, el maximo tiempo de supervivencia fue {} segundos"
        # .format(max_survival_time))
        return 4, max_survival_time
    elif len(a[0]) == 3:
        # print("3 jugadores quedaron vivos, el maximo tiempo de supervivencia fue {} segundos".
        # format(max_survival_time))
        return 3, max_survival_time
    elif len(a[0]) == 2:
        # print("2 jugadores quedaron vivos, el maximo tiempo de supervivencia fue {} segundos".
        # format(max_survival_time))
        return 2, max_survival_time
    else:
        # print("1 jugador quedo vivo, el maximo tiempo de supervivencia fue {} segundos".format(max_survival_time))
        return 1, max_survival_time


def get_time_survival_and_survivors(teams_new, positions, survival_time):
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

    return players_alive_list, max_survival_time_list


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


def get_statistics_for_best_teams(item, teams_new, positions, word):
    # object_sing = "content"
    statistics_teams = item
    """    if word == "kills":
            object_sing = "ELIMINACIONES"
        elif word == "damage":
            object_sing = "DAÑOS"
        elif word == "damage":
            object_sing = "daño"
        elif word == "resurrects":
            object_sing = "RESURRECCIONES"
            statistics_teams = get_sum_item_for_teams(item)
        elif word == "assists":
            object_sing = "ASISTENCIAS"
    """
    statistic_total_list = [[statistics_teams[teams_new.index(positions[0][1])], positions[0][1]],
                            [statistics_teams[teams_new.index(positions[1][1])], positions[1][1]],
                            [statistics_teams[teams_new.index(positions[2][1])], positions[2][1]]]
    # print("{} DE LOS EQUIPOS ".format(object_sing), statistic_total_list)
    return statistic_total_list


def xb_score(revived_total_list, damage_for_bests_teams, kills_for_bests_teams, num_players_alive,
             assists_for_best_teams, index):
    punt_resurr = 10 - revived_total_list[index][0]

    punt_damage = 0
    if max(damage_for_bests_teams) == damage_for_bests_teams[0]:
        punt_damage = 10
    elif max(damage_for_bests_teams) == damage_for_bests_teams[1]:
        punt_damage = 7
    elif max(damage_for_bests_teams) == damage_for_bests_teams[2]:
        punt_damage = 5

    punt_kills = (kills_for_bests_teams[index][0] / 18) * 10
    punt_assists = (assists_for_best_teams[index][0] / max(assists_for_best_teams)[0]) * 10

    punt_players_alive = 0

    if num_players_alive[index] == 4:
        punt_players_alive = 10
    elif num_players_alive[index] == 3:
        punt_players_alive = 8
    elif num_players_alive[index] == 2:
        punt_players_alive = 6
    elif num_players_alive[index] == 1:
        punt_players_alive = 4

    x_booyah = (punt_players_alive + punt_kills + punt_damage + punt_resurr + punt_assists) / 50
    print("El score para {} es:".format(revived_total_list[index][1]))
    print(f"{x_booyah:.2f}\n")

    return x_booyah


def xb_philosophy(score_list, teams_new, damage_total_list, total_kills_list, revived_times, assists, survival_time):
    positions = heapq.nlargest(3, zip(score_list, teams_new))
    print("POSICIONES DE LOS EQUIPOS", positions)

    # Obteniendo las veces que usaron la resurreccion
    revived_total_list = get_statistics_for_best_teams(revived_times, teams_new, positions, "resurrects")

    damage_for_bests_teams = get_statistics_for_best_teams(damage_total_list, teams_new, positions, "damage")

    kills_for_bests_teams = get_statistics_for_best_teams(total_kills_list, teams_new, positions, "kills")

    # Asistencias totales de los equipos
    assists_new = get_sum_item_for_teams(assists)

    assists_for_best_teams = get_statistics_for_best_teams(assists_new, teams_new, positions, "assists")

    num_players_alive, max_survival_time = get_time_survival_and_survivors(teams_new, positions, survival_time)
    list_score = []
    for index in range(0, 3):
        x_booyah = xb_score(revived_total_list, damage_for_bests_teams, kills_for_bests_teams, num_players_alive,
                            assists_for_best_teams, index)
        list_score.append(x_booyah)
    return list_score, positions


def main_philosophy(path_file):
    df = pd.read_csv(path_file, header=0)
    teams = list(df["team_name"])
    total_kills = list(df["killing_score"])
    assists = list(df["assists"])
    damages = list(df["damage"])
    survival_time = list(df["survival_time"])
    score = list(df["ranking_score"])
    revived_times = list(df["revived_times"])

    # Sacando una tabla de los 12 equipos
    teams_new = get_one_item_for_teams(teams)

    # Sacando las kills totales por cada equipo
    total_kills_list = get_one_item_for_teams(total_kills)

    # Obteniendo el equipo com mas daño
    damage_total_list = get_sum_item_for_teams(damages)

    # Sacando el daño total por equipo
    score_list = get_one_item_for_teams(score)

    titulo = "EXPECTATIVE BOOYAH PHILOSOPHY"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    list_score, positions = xb_philosophy(score_list, teams_new, damage_total_list, total_kills_list,
                                          revived_times, assists, survival_time)
    return list_score, positions


def get_xbooyah_per_day(path, name_list, xbooyah_list, day):
    path += "Jornada_" + day + "\\"
    maps_number = 6
    for a in range(1, maps_number + 1):
        path_file = path + str(a) + ".csv"
        print("Partida {}".format(a))
        list_score, positions = main_philosophy(path_file)
        for index in range(0, 3):
            if positions[index][1] in name_list:
                xbooyah_list[name_list.index(positions[index][1])] += list_score[index]
            else:
                name_list.append(positions[index][1])
                xbooyah_list.append(list_score[index])

    maxim_xbooyah = heapq.nlargest(3, zip(xbooyah_list, name_list))

    print("{} tiene el mejor xBooyah".format(maxim_xbooyah[0][1]))
    print(f"{maxim_xbooyah[0][0]:.2f}\n")
    print("{} tiene el segundo mejor xBooyah".format(maxim_xbooyah[1][1]))
    print(f"{maxim_xbooyah[1][0]:.2f}\n")
    print("{} tiene el tercer mejor xBooyah".format(maxim_xbooyah[2][1]))
    print(f"{maxim_xbooyah[2][0]:.2f}\n")


def get_xbooyah_per_game(path, day):
    name = input("Ingresa el numero de la partida: ")
    path_file = path + "Jornada_" + day + "\\" + name + ".csv"
    main_philosophy(path_file)


def get_max_xbooyah(choice, path):
    name_list = []
    xbooyah_list = []
    if choice in ["t", "T"]:
        day = input("Ingresa el numero de la jornada que se juega: ")
        get_xbooyah_per_day(path, name_list, xbooyah_list, day)

    elif choice in ["u", "U"]:
        day = input("Ingresa el numero de la jornada que se juega: ")
        get_xbooyah_per_game(path, day)


def main():
    titulo = "EXPECTATIVE BOOYAH PHILOSOPHY"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    path = ".\\partidas\\"
    choice = input("¿Quieres conocer el xBooyah de [t]oda la jornada o [u]na sola partida? ")
    while choice not in ["t", "T", "u", "U"]:
        print("Escoge de nuevo")
        choice = input("¿Quieres conocer el xBooyah de [t]oda la jornada o [u]na sola partida? ")

    get_max_xbooyah(choice, path)


if __name__ == "__main__":
    main()

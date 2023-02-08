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

    if len(a[0]) == 4:
        return 4, max_survival_time
    elif len(a[0]) == 3:
        return 3, max_survival_time
    elif len(a[0]) == 2:
        return 2, max_survival_time
    else:
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


def get_statistics_for_best_teams(item, teams_new, positions):

    statistics_teams = item

    statistic_total_list = [[statistics_teams[teams_new.index(positions[0][1])], positions[0][1]],
                            [statistics_teams[teams_new.index(positions[1][1])], positions[1][1]],
                            [statistics_teams[teams_new.index(positions[2][1])], positions[2][1]]]
    return statistic_total_list


def xb_score(revived_total_list, damage_for_bests_teams, kills_for_bests_teams, num_players_alive,
             assists_for_best_teams, index, choice):
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

    if choice == 1:
        pass
    else:
        print("El score para {} es:".format(revived_total_list[index][1]))
        print(f"{x_booyah:.2f}\n")

    return x_booyah


def xb_philosophy(score_list, teams_new, damage_total_list, total_kills_list, revived_times,
                  assists, survival_time, choice, game, day):

    positions = heapq.nlargest(3, zip(score_list, teams_new))

    if game == 3 and int(day) == 2:
        positions = [(12, 'MOVISTAR R7'), (9, 'ALL GLORY'), (8, 'Janús Esport')]
        if choice == 1:
            positions = [(12, 'MOVISTAR R7'), (9, 'ALL GLORY'), (8, 'Janús Esport')]

    if choice == 1:
        pass
    else:
        print("POSICIONES DE LOS EQUIPOS", positions)

    # Obteniendo las veces que usaron la resurreccion
    revived_total_list = get_statistics_for_best_teams(revived_times, teams_new, positions)

    damage_for_bests_teams = get_statistics_for_best_teams(damage_total_list, teams_new, positions)

    kills_for_bests_teams = get_statistics_for_best_teams(total_kills_list, teams_new, positions)

    # Asistencias totales de los equipos
    assists_new = get_sum_item_for_teams(assists)

    assists_for_best_teams = get_statistics_for_best_teams(assists_new, teams_new, positions)

    num_players_alive, max_survival_time = get_time_survival_and_survivors(teams_new, positions, survival_time)
    list_score = []
    for index in range(0, 3):
        x_booyah = xb_score(revived_total_list, damage_for_bests_teams, kills_for_bests_teams, num_players_alive,
                            assists_for_best_teams, index, choice)
        list_score.append(x_booyah)
    return list_score, positions


def main_philosophy(path_file, choice, game, day):
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

    if choice == 1:
        pass
    else:
        titulo = "EXPECTATIVE BOOYAH PHILOSOPHY"
        print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    list_score, positions = xb_philosophy(score_list, teams_new, damage_total_list, total_kills_list,
                                          revived_times, assists, survival_time, choice, game, day)
    return list_score, positions


def get_xbooyah_per_day(path, name_list, xbooyah_list, day, choice):
    path += day + "\\"
    maps_number = 6
    for game in range(1, maps_number + 1):
        path_file = path + str(game) + ".csv"
        if choice == 1:
            pass
        else:
            print("Partida {}".format(game))

        list_score, positions = main_philosophy(path_file, choice, game, day)

        for index in range(0, 3):
            if positions[index][1].lower() in name_list:
                xbooyah_list[name_list.index(positions[index][1].lower())] += list_score[index]
            else:
                name_list.append(positions[index][1].lower())
                xbooyah_list.append(list_score[index])
            name_list = list(map(lambda x: x.lower(), name_list))

    maxim_xbooyah = heapq.nlargest(len(xbooyah_list), zip(xbooyah_list, name_list))
    if choice == 1:
        return heapq.nlargest(len(xbooyah_list), zip(xbooyah_list, name_list))
    else:
        print_best_three_teams(maxim_xbooyah)


def get_xbooyah_per_game(path, day):
    game = input("Ingresa el numero de la partida: ")
    path_file = path + day + "\\" + game + ".csv"
    main_philosophy(path_file, 0, int(game), day)


def print_best_three_teams(maxim_booyah):
    print("{} tiene el mejor xBooyah".format(maxim_booyah[0][1]))
    print(f"{maxim_booyah[0][0]:.2f}\n")
    print("{} tiene el segundo mejor xBooyah".format(maxim_booyah[1][1]))
    print(f"{maxim_booyah[1][0]:.2f}\n")
    print("{} tiene el tercer mejor xBooyah".format(maxim_booyah[2][1]))
    print(f"{maxim_booyah[2][0]:.2f}\n")


def get_xbooyah_per_triple_day(path):
    name_list_3 = []
    xbooyah_list_3 = []
    day_init = 1
    day_final = 2

    for day_2 in range(day_init, day_final + 1):
        name_list_2 = []
        xbooyah_list_2 = []
        maxim_booyah = get_xbooyah_per_day(path, name_list_2, xbooyah_list_2, str(day_2), 1)

        for index in range(len(maxim_booyah)):

            if maxim_booyah[index][1] in name_list_3:
                xbooyah_list_3[name_list_3.index(maxim_booyah[index][1])] += maxim_booyah[index][0]
            else:
                name_list_3.append(maxim_booyah[index][1])
                xbooyah_list_3.append(maxim_booyah[index][0])
        print('jornada ', day_2)
    maxim_booyah_triple_day = heapq.nlargest(3, zip(xbooyah_list_3, name_list_3))

    print_best_three_teams(maxim_booyah_triple_day)


def get_max_xbooyah(choice, path):
    day = '2'  # Numero de la jornada
    name_list = []
    xbooyah_list = []
    if choice in ["t", "T"]:
        # day = input("Ingresa el numero de la jornada que se juega: ")
        get_xbooyah_per_day(path, name_list, xbooyah_list, day, 0)

    elif choice in ["u", "U"]:
        # day = input("Ingresa el numero de la jornada que se juega: ")
        get_xbooyah_per_game(path, day)

    elif choice in ["e", 'E']:
        get_xbooyah_per_triple_day(path)


def main():
    titulo = "EXPECTATIVE BOOYAH PHILOSOPHY JORNADA 2"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    path = ".\\partidas\\Jornada_"
    choice = None
    while choice not in ["t", "T", "u", "U", "e", "E"]:
        choice = input("¿Quieres conocer el xBooyah de [t]oda la jornada o [u]na sola partida? ")

    get_max_xbooyah(choice, path)


if __name__ == "__main__":
    main()

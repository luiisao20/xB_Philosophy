import heapq
import numpy as np
import pandas as pd


def get_info_from_file(path, word):
    df = pd.read_csv(path, header=0)
    return list(df[word])


def get_name_from_file(path):
    df = pd.read_csv(path, header=0)
    return list(df["nickname"])


def maximum(path, word):

    items = get_info_from_file(path, word)
    name = get_name_from_file(path)

    object_sing = "content"
    if word == "kills":
        object_sing = "eliminaciones"
    elif word == "assists":
        object_sing = "asitencias"
    elif word == "damage":
        object_sing = "daño"
    elif word == "medkit_use":
        object_sing = "botiquines usados"
    elif word == "revive_teammate_times":
        object_sing = "compañeros revividos"
    elif word == "knock_down":
        object_sing = "derribos"
    elif word == "headshots":
        object_sing = "disparos a la cabeza"
    elif word == "grenade_use":
        object_sing = "granadas desplegadas"

    max_item = heapq.nlargest(3, zip(items, name))
    names = []
    achievements = []
    index = 0
    for item in max_item:
        names.append(item[1])
        achievements.append(item[0])
        index += 1

    print("Los 3 jugadores con más {} son:\n"
          "{} con {} {}\n"
          "{} con {} {}\n"
          "{} con {} {}\n".format(object_sing, names[0], achievements[0], object_sing,
                                  names[1], achievements[1], object_sing,
                                  names[2], achievements[2], object_sing))


def minimum(path, word):
    object_sing = "tiempo de supervivencia"

    items = get_info_from_file(path, word)
    name = get_name_from_file(path)

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


def get_one_item_for_teams(path, word):
    item = get_info_from_file(path, word)
    item_new = []
    for a in range(48):
        if a % 4 == 0:
            item_new.append(item[a])
        else:
            pass
    return item_new


def get_sum_item_for_teams(path, word):
    item = get_info_from_file(path, word)
    e = 0
    f = 4
    item_total = []
    for c in range(12):
        d = slice(e, f)
        item_total.append(sum(item[d]))
        e += 4
        f += 4
    return item_total


def teams_statistics(path):
    # Sacando una tabla de los 12 equipos
    teams_new = get_one_item_for_teams(path, "team_name")

    # Sacando las kills totales por cada equipo
    total_kills_list = get_one_item_for_teams(path, "killing_score")

    # Obteniendo el equipo com mas daño
    damage_total_list = get_sum_item_for_teams(path, "damage")

    # Daño máximo de partida
    highest_damages_teams = heapq.nlargest(3, zip(damage_total_list, teams_new))
    print("DAÑO MÁS ALTOS", highest_damages_teams)

    kills_for_bests_teams = heapq.nlargest(3, zip(total_kills_list, teams_new))

    print("EQUIPOS CON MÁS KILLS", kills_for_bests_teams)


def main():
    titulo = "DATOS POR JUGADORES, ELIGIENDO LOS MEJORES 3"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    day = input("Ingresa el numero de jornada que se juega: ")

    name = input("Ingresa el numero de partida que quieres concer: ")

    path = ".\\partidas\\Jornada_" + day + "\\" + name + ".csv"

    # Jugador con menos tiempo de supervivencia
    minimum(path, "survival_time")
    # Jugador con mas granadas desplegadas
    maximum(path, "grenade_use")

    # Jugador con mas disparos a la cabeza
    maximum(path, "headshots")

    # Jugador con mas derribos
    maximum(path, "knock_down")

    # Jugador que mas revivio
    maximum(path, "revive_teammate_times")

    # El jugador con mas botiquines usados
    maximum(path, "medkit_use")

    # Sacando el jugador con más kills
    maximum(path, "kills")

    # Sacando el jugador con más daño
    maximum(path, "damage")

    # Sacando el jugador con más asistencias
    maximum(path, "assists")

    titulo = "DATOS POR EQUIPOS"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

    # Sacando estadísticas de los equipos en conjunto
    teams_statistics(path)


if __name__ == "__main__":
    main()

import pandas as pd


def get_statistics_for_players(day, game):
    path = "partidas\\Jornada_" + day + "\\" + game + ".csv"
    df = pd.read_csv(path, header=0)
    names = list(df["nickname"])
    kills = list(df["kills"])
    assists = list(df["assists"])
    headshot_kill_times = list(df["headshot_killtimes"])
    damage = list(df["damage"])
    grenade_use = list(df['grenade_use'])
    revived_times = list(df['revived_times'])
    revive_teammate_times = list(df['revive_teammate_times'])

    return names, kills, assists, headshot_kill_times, damage, grenade_use, revived_times, revive_teammate_times


def put_players_in_list_per_game(all_players, names, kills, assists, headshot_kill_times, damage, index, names_list,
                                 grenade_use, revived_times, revive_teammate_times):
    new_player = {
        "name": names[index],
        "kills": kills[index],
        "assists": assists[index],
        "headshot_kill_times": headshot_kill_times[index],
        "damage": damage[index],
        "games_played": 0,
        "grenade_use": grenade_use[index],
        "revived_times": revived_times[index],
        'revive_teammate_times': revive_teammate_times[index]
    }
    new_player["games_played"] += 1
    all_players.append(new_player)
    names_list.append(new_player["name"])


def update_statistics_for_each_player(all_players, index_player, index_2, kills, assists, headshot_kill_times, damage,
                                      grenade_use, revived_times, revive_teammate_times):

    all_players[index_player]["kills"] += kills[index_2]
    all_players[index_player]["assists"] += assists[index_2]
    all_players[index_player]["headshot_kill_times"] += headshot_kill_times[index_2]
    all_players[index_player]["damage"] += damage[index_2]
    all_players[index_player]["games_played"] += 1
    all_players[index_player]['grenade_use'] += grenade_use[index_2]
    all_players[index_player]['revive_teammate_times'] += revive_teammate_times[index_2]
    all_players[index_player]['revived_times'] += revived_times[index_2]


def get_all_players_list(day):
    maps_number = 6
    all_players = []
    names_list = []

    for index in range(1, maps_number + 1):
        game = str(index)
        names, kills, assists, headshot_kill_times, damage, grenade_use, revived_times, revive_teammate_times \
            = get_statistics_for_players(day, game)

        for index_2 in range(len(names)):

            if names[index_2] in names_list:
                index_player = names_list.index(names[index_2])
                update_statistics_for_each_player(all_players, index_player, index_2, kills, assists,
                                                  headshot_kill_times, damage, grenade_use, revived_times,
                                                  revive_teammate_times)
            else:
                put_players_in_list_per_game(all_players, names, kills, assists, headshot_kill_times, damage, index_2,
                                             names_list, grenade_use, revived_times, revive_teammate_times)
    put_rates(all_players)
    return all_players, names_list


def put_rates(all_players):
    for index in range(len(all_players)):
        all_players[index]["KDA_rate"] = (all_players[index]["kills"] + all_players[index]["assists"]) / \
                                         all_players[index]["games_played"]
        if all_players[index]["kills"] != 0:
            percentage = int(all_players[index]["headshot_kill_times"] * 100 / all_players[index]["kills"])
            all_players[index]["headshot_rate"] = str(percentage) + "%"
        else:
            all_players[index]["headshot_rate"] = "0 %"

    return all_players


def get_best_players_and_statistics(all_players, word):
    sorted_dict_list = sorted(all_players, key=lambda x: x[word], reverse=True)
    top_two_names = [(d['name'], d[word], d['games_played']) for d in sorted_dict_list[:3]]

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

    print(top_two_names)


def get_best_statistics_per_day(all_players):
    print("\nPorcentaje de disparo a la cabeza")
    get_best_players_and_statistics(all_players, "headshot_rate")

    print("\nKD")
    get_best_players_and_statistics(all_players, "KDA_rate")

    print("\nDaño")
    get_best_players_and_statistics(all_players, "damage")

    print("\nEliminaciones")
    get_best_players_and_statistics(all_players, "kills")

    print("\nAsistencias")
    get_best_players_and_statistics(all_players, "assists")

    print('\nCompaneros revividos')
    get_best_players_and_statistics(all_players, 'revive_teammate_times')

    print('\nVeces revivido')
    get_best_players_and_statistics(all_players, 'revived_times')

    print('\nGranadas usadas')
    get_best_players_and_statistics(all_players, 'grenade_use')


def get_all_players_list_in_days():

    names_list_new = []
    all_players_complete = []
    day = 2
    for index in range(1, day + 1):
        all_players, names_list = get_all_players_list(str(index))

        for sub_index in range(len(all_players)):

            if all_players[sub_index]['name'] not in names_list_new:
                all_players_complete.append(all_players[sub_index])
                names_list_new.append(names_list[sub_index])
            else:
                pass

    names_list_test = []
    for index_2 in range(len(all_players_complete)):
        names_list_test.append(all_players_complete[index_2]['name'])

    return all_players_complete


def main():

    choice = input("Escoger estadisticas por [U]na jornada o [V]arias: ")

    if choice in ['u', 'U']:
        day = input("Ingresa la jornada que se juega: ")
        all_players = get_all_players_list(day)
        get_best_statistics_per_day(all_players)

    elif choice in ['v', 'V']:
        all_players = get_all_players_list_in_days()


if __name__ == "__main__":
    main()

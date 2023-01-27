import ast
import heapq
import pandas as pd


def statistics_for_weapon(weapon_usages, word):
    weapon_name = []
    kills_weapon = []
    for index in range(0, len(weapon_usages)):
        wn = weapon_usages[index]
        w_new = ast.literal_eval(wn)
        for a in range(0, len(w_new)):
            if w_new[a]["weapon_name"] in weapon_name:
                kills_weapon[weapon_name.index(w_new[a]["weapon_name"])] += w_new[a][word]
            else:
                weapon_name.append(w_new[a]["weapon_name"])
                kills_weapon.append(w_new[a][word])

    return weapon_name, kills_weapon


def get_statistics_for_day(path, word):
    weapon_name_final = []
    item_weapon_final = []

    for a in range(1, 9):
        path_file = path + str(a) + ".csv"
        df = pd.read_csv(path_file, header=0)
        weapon_usages = list(df["weapon_usages"])
        weapon_name, item_weapon = statistics_for_weapon(weapon_usages, word)
        for b in range(0, len(weapon_name)):
            if weapon_name[b] in weapon_name_final:
                item_weapon_final[weapon_name_final.index(weapon_name[b])] += item_weapon[b]
            else:
                weapon_name_final.append(weapon_name[b])
                item_weapon_final.append(item_weapon[b])
    print("Las 3 armas con más {} de la jornada son {}".format(word, heapq.nlargest(3, zip(
        item_weapon_final, weapon_name_final))))


def get_statistics_for_game(weapon_usages, word):
    weapon_name, kills_weapon = statistics_for_weapon(weapon_usages, word)
    print("Las 3 armas con más {} de la partida son {}".format(word, heapq.nlargest(3, zip(
        kills_weapon, weapon_name))))


def main():
    path = ".\\partidas\\"
    choice = input("¿Deseas hacer de [T]odos los archivos o solo [U]no?: ")

    while choice not in ["U", "T", "u", "t"]:
        print("Escoge de nuevo")
        choice = input("¿Deseas hacer de [T]odos los archivos o solo [U]no?: ")

    if choice in ["T", "t"]:
        get_statistics_for_day(path, "kills")
        get_statistics_for_day(path, "damage")
        get_statistics_for_day(path, "headshots")

    elif choice in ["U", "u"]:
        name = input("Ingresa el número de partida que quieres conocer: ")
        path_file = path + name + ".csv"
        df = pd.read_csv(path_file, header=0)
        weapon_usages = list(df["weapon_usages"])
        get_statistics_for_game(weapon_usages, "kills")
        get_statistics_for_game(weapon_usages, "damage")
        get_statistics_for_game(weapon_usages, "headshots")


if __name__ == "__main__":
    main()

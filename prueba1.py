import heapq
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
    elif word == "damages":
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
          "{} con {} {}\n". format(object_sing, names[0], kills[0], object_sing,
                                   names[1], kills[1], object_sing,
                                   names[2], kills[2], object_sing))


def main():
    total_kills = list(df["killing_score"])
    assists = list(df["assists"])
    damages = list(df["damage"])
    kills = list(df["kills"])
    med_kit = list(df["medkit_use"])
    maximum(kills, "kills")
    maximum(assists, "assists")
    maximum(damages, "damages")
    a = heapq.nlargest(3, zip(kills, name))
    h = list(a[0])
    print(heapq.nlargest(3, zip(kills, name)))
    print(heapq.nlargest(3, zip(damages, name)))

    a = [5, 9, 10, 11, 12]
    b = ["hol", "aje", "ale", "lui", "one"]
    print(heapq.nlargest(3, zip(a, b)))


if __name__ == "__main__":
    main()

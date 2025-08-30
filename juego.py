import random  # Texto random


def game(a, b):
    if a == b:
        print("empate!")
        return int(0)

    elif a == "1" and b == "2":
        print("papel le gana a piedra")
        return 1
    elif a == "1" and b == "3":
        print("tijera le gana  a papel")
        return 2
    elif a == "2" and b == "1":
        print("papel le gana a piedra")
        return 2
    elif a == "2" and b == "3":
        print("piedra le gana a tijeras")
        return 1
    elif a == "3" and b == "2":
        print("piedra le gana a tijeras")
        return 2
    elif a == "3" and b == "4":
        print("tijera corta la lagartija a la mitad")
        return 1
    elif a == "3" and b == "5":
        print("spock destroza las tijeras")
        return 2
    elif a == "4" and b == "5":
        print("lagartija envenena a spock")
        return 1
    elif a == "4" and b == "2":
        print("la piedra aplasta a la lagartija")
        return 2


print("\n Bienvenido a DCCachipun")


print("-" * 26 + " MENU " + "-"*26)
print("[1] Papel")
print("[2] Piedra")
print("[3] Tijeras")
print("[4] Lagartija")
print("[5] spock \n")


jugar = True
games = [0, 0, 0]
while (jugar):
    a = input("Jugador 1:")
    b = str(random.randint(1, 4))
    ganador = game(a, b)
    games[ganador] += 1

    if games[1] < games[2]:
        print(f"has ganado {games[1]}:{games[2]}")

    elif games[1] > games[2]:
        print(f"ha ganado la computadora {games[1]}:{games[2]}")

import random


def game(a, b):
    if a == b:
        print("empate!")
        return 0

    elif a == "1" and b == "2":
        print("papel le gana a piedra")
        return 1
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
        print("piedra le gana a tijeras")
        return 2


print("Bienvenido a DCCorta")


print("-" * 26 + " MENU " + "-"*26)
print("[1] Papel")
print("[2] Piedra")
print("[3] Tijeras")
print("[4] Lagartija")
print("[5] spock \n")


jugar = True
games = [0,0,0]
while(jugar):
    jugador_1 = input("Jugador 1:")
    a = 1
    b = random.randint(1, 5)
    ganador = game(a, b)
    games[ganador]+=1


















    if games[1] > games [2]:
        print(f"ha ganado la computadora")

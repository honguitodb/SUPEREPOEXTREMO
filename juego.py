import random


def game(a, b):
    pass


print("Bienvenido a DCCorta")


print("-" * 26 + " MENU " + "-"*26)
print("[1] Papel")
print("[2] Piedra")
print("[3] Tijeras")
print("[4] Lagartija")
print("[5] spock \n")


jugar = True

while (jugar):
    jugador_1 = int(input("Jugador 1:"))
    jugador_2 = int(input("Jugador 2:"))
    ganador = game(jugador_1, jugador_2)
    contador_1 = 0
    contador_2 = 0
    if ganador == 1:
        contador_1 += 1
        print("Gano jugador 1")
    elif ganador == 2:
        contador_2 += 1
        print("Gano jugador 2")
    else:
        print("Empate")

    print(f"Puntos jugador 1: {contador_1}")
    print(f"Puntos jugador 2: {contador_2}")

jueguito = []

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
jueguito = []
while(jugar):
    jugador_1 = int(input("Jugador 1:"))
    jugador_2 = int(input("Jugador 2:"))
    ganador = game(jugador_1, jugador_2)
    print(jueguito[ganador])


    
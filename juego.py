import random 

def game(a, b):
    if a == b:
        return 0
    elif a == "1" and b == "2":
        return 1
    elif a == "2" and b == "1":
        return 2
    #elif 





















print("Bienvenido a DCCorta")


print("-" * 26 + " MENU " + "-"*26)
print("[1] Papel")
print("[2] Piedra")
print("[3] Tijeras")
print("[4] Lagartija")
print("[5] spock \n")





jugar = True
while(jugar):
    jugador_1 = input("Jugador 1:")
    a = 1
    b = 2
    game(a, b)

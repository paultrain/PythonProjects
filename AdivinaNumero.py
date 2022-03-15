import random


def adivinar(x):
    random_numero = random.randint(1, x)
    adivina = 0
    while adivinar != random_numero:
        adivina = int(input(f"adivina un numero entre 1 y {x}: "))
        if adivina < random_numero:
            print("Perdona, adivina de nuevo. Muy bajo.")
        elif adivina > random_numero:
            print("Perdona, adivina de nuevo. Muy alto.")
        else:
            print(
                f"Felicidades!!!. Adivinaste el numero {random_numero}"
                "correctamente.")


def computadora_adivina(x):
    bajo = 1
    alto = x
    devolucion = ''
    while devolucion != 'c':
        if bajo != alto:
            adivina = random.randint(bajo, alto)
        else:
            adivina = bajo  # tambien podria ser alto.
        devolucion = input(
            f"Es {adivina} muy alto (A), muy bajo(B), o correcta(C)?").lower()
        if devolucion == 'a':
            alto = adivina - 1
        elif devolucion == 'b':
            bajo = adivina + 1
        else:
            print(f"Bien! La computadora adivinó tu numero: {adivina}"
                  "correctamente!!!")


# adivinar(10)
computadora_adivina(10)

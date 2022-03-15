import time

print("Hola! Bienvenido a la Calculadora MK II")
time.sleep(1)

num1 = int(input("Dime el primer numero: "))
num2 = int(input("ok, ahora dime un segundo numero: "))

print(f"Bien, elegiste los numeros: {num1} y {num2}")
time.sleep(1)

simbolo = input(
    "¿Que operacion quieres realizar con estos numeros? (Escribe la primera"
    "letra)\n -Sumar\n -Restar\n -Multiplicar\n -Dividir\n")


if simbolo == "s" or simbolo == "S":
    print(f"{num1} + {num2} =", (num1 + num2))
elif simbolo == "r" or simbolo == "R":
    print(f"{num1} - {num2} =", (num1 - num2))
elif simbolo == "m" or simbolo == "M":
    print(f"{num1} * {num2} =", (num1 * num2))
elif simbolo == "d" or simbolo == "D":
    print(f"{num1} / {num2} =", (num1 / num2))
else:
    print("No has escrito ninguna letra correcta\nS|s para sumar, R|r para"
          "restar, M|m para multiplicar o D|d para dividir")

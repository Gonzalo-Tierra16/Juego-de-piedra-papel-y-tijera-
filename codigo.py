import random

puntos_usuario = 0
puntos_maquina = 0
opciones = ["piedra", "papel", "tijeras"]

print("Bienvenido a Piedra, Papel o Tijeras")
print("Escribe 'salir' para terminar el juego.\n")

while True:
    eleccion = input("Elige piedra, papel o tijeras: ").lower()

    if eleccion == "salir":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break

    elif eleccion not in opciones:
        print("Opción inválida. Intenta de nuevo.\n")
        continue

    CPU = random.choice(opciones)
    print(f"El CPU eligió: {CPU}")

    if eleccion == CPU:
        print("¡Es un empate!\n")
    elif (
        (eleccion == "piedra" and CPU == "tijeras") or
        (eleccion == "papel" and CPU == "piedra") or
        (eleccion == "tijeras" and CPU == "papel")
    ):
        print("¡Excelente! ¡Ganaste esta ronda!\n")
        puntos_usuario += 1
    else:
        print("¡Perdiste esta ronda!\n")
        puntos_maquina += 1

    print(f"Puntaje - Tú: {puntos_usuario} / Puntos del CPU: {puntos_maquina}\n")

print("\nResultado final:")
if puntos_usuario > puntos_maquina:
    print("¡Muy bien jugado! ¡Ganaste el juego!")
    print(f"Tú puntaje: {puntos_usuario} / Puntos del CPU: {puntos_maquina}")
elif puntos_usuario < puntos_maquina:
    print("El CPU ganó el juego.")
    print(f"Tú puntaje: {puntos_usuario} / Puntos del CPU: {puntos_maquina}")
else:
    print("El juego terminó en un empate ¡Felicidades a ambos!")
    print(f"Tú puntaje: {puntos_usuario} / Puntos del CPU: {puntos_maquina}")
    
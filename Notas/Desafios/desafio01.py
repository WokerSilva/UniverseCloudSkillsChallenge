## Autor : Marco Silva Huerta 
## Juego de piedra, papel o tijeras 
import random

def jugar_piedra_papel_tijeras(computadora, usuario):
    # Definir las opciones válidas
    opciones = ["piedra", "papel", "tijeras"]

    # Validar las selecciones de los jugadores
    if computadora not in opciones or usuario not in opciones:
        return "¡Selección no válida! Debes elegir entre piedra, papel o tijeras."

    # Determinar al ganador
    if computadora == usuario:
        return "¡Es un empate!"
    elif (
        (computadora == "piedra" and usuario == "tijeras") or
        (computadora == "papel" and usuario == "piedra") or
        (computadora == "tijeras" and usuario == "papel")
    ):
        return "¡La computadora ha ganado!"
    else:
        return "¡El usuario ha ganado!"

while True:
    # Obtener la selección del usuario
    usuario = input("Elige piedra, papel o tijeras (o 'salir' para salir): ").lower()

    if usuario == 'salir':
        print("¡Gracias por jugar! Hasta luego.")
        break

    # Generar la selección aleatoria de la computadora
    computadora = random.choice(["piedra", "papel", "tijeras"])

    # Mostrar las selecciones de ambos jugadores
    print(f"Computadora eligió: {computadora}")
    print(f"Usuario eligió: {usuario}")

    # Determinar el resultado del juego
    resultado = jugar_piedra_papel_tijeras(computadora, usuario)
    print(resultado)

    # Preguntar al usuario si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if jugar_de_nuevo != 'si':
        print("¡Gracias por jugar! Hasta luego.")
        break

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
        return "¡La computadora a ganado!"
    else:
        return "¡El usuario a ganado!"

# Obtener la selección del usuario
usuario = input("Elige piedra, papel o tijeras: ").lower()

# Generar la selección aleatoria de la computadora
computadora = random.choice(["piedra", "papel", "tijeras"])

# Mostrar las selecciones de ambos jugadores
print(f"Computadora eligió: {computadora}")
print(f"Usuario eligió: {usuario}")

# Determinar el resultado del juego
resultado = jugar_piedra_papel_tijeras(computadora, usuario)
print(resultado)
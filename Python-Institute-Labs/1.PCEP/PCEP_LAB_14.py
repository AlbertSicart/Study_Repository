secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

# Pedimos al usuario que ingrese un número
numero = int(input("Ingresa un número entero: "))

# Usamos un bucle while para repetir la solicitud hasta que el usuario adivine el número secreto
while numero != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Introduce un número entero de nuevo: "))

# Cuando el usuario adivine el número, salimos del bucle y mostramos el siguiente mensaje
print("¡Bien hecho, muggle! Eres libre ahora.")

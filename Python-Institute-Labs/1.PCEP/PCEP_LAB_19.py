# Leer un número natural.
c0 = int(input("Ingresa un número natural: "))

# Validar que el número ingresado sea positivo
if c0 <= 0:
    print("¡El número debe ser positivo!")
else:
    # Inicializar contador de pasos
    pasos = 0
    
    # Mientras c0 sea diferente de 1, aplicar las operaciones de Collatz
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:  # Si c0 es par
            c0 = c0 // 2
        else:  # Si c0 es impar
            c0 = 3 * c0 + 1
        pasos += 1
        
    # Imprimir el último valor de c0 (que debería ser 1)
    print(c0)
    # Imprimir el número total de pasos
    print("pasos =", pasos)

def is_prime(num):
    # 0 y 1 no son números primos
    if num < 2:
        return False
    # 2 es un número primo
    elif num == 2:
        return True
    # Todos los números pares excepto 2 no son primos
    elif num % 2 == 0:
        return False
    # Comprobamos divisores desde 3 hasta la raíz cuadrada de num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Probamos la función con números desde 2 hasta 19
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

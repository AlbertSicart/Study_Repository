my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Creamos un conjunto vacío para almacenar los números que ya hemos visto.
vistos = set()

# Creamos una lista vacía para almacenar la lista final sin duplicados.
lista_sin_duplicados = []

# Recorremos cada número en la lista original.
for numero in my_list:
    # Si el número no ha sido visto antes, lo añadimos a la lista final y al conjunto de vistos.
    if numero not in vistos:
        vistos.add(numero)
        lista_sin_duplicados.append(numero)

# Actualizamos my_list para que contenga los elementos sin duplicados.
my_list = lista_sin_duplicados

print("La lista con elementos únicos:")
print(my_list)

# Ingresa un valor flotante para la variable a aquí
a = float(input("Introduce un valor para a: "))

# Ingresa un valor flotante para la variable b aquí
b = float(input("Introduce un valor para b: "))

# Muestra el resultado de la suma aquí 
print("La suma de a y b es:", a + b)

# Muestra el resultado de la resta aquí
print("La resta de a y b es:", a - b)

# Muestra el resultado de la multiplicación aquí
print("La multiplicación de a y b es:", a * b)

# Muestra el resultado de la división aquí
# Aseguramos que b no es 0 para evitar la división entre cero.
if b != 0:
    print("La división de a entre b es:", a / b)
else:
    print("Error: División entre cero.")

print("\n¡Eso es todo, amigos!")

def read_int(prompt, min, max):
    while True:
        try:
            # Intentar convertir la entrada del usuario en un número entero
            valor = int(input(prompt))
            # Si el valor está fuera del rango, se levanta un error
            if valor < min or valor > max:
                raise ValueError
            # Si todo es correcto, se devuelve el valor
            return valor
        except ValueError:
            if isinstance(valor, int):
                print(f"Error: el valor no está dentro del rango permitido ({min}..{max})")
            else:
                print("Error: entrada incorrecta")

v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)
print("El número es:", v)

year = int(input("Introduce un año:"))

# Verificamos si el año es anterior al inicio del calendario Gregoriano
if year < 1582:
    print("No está dentro del período del calendario Gregoriano")
# Si el año no es divisible por 4 (usando el operador % para obtener el resto)
elif year % 4 != 0:
    print("Año Común")
# Si el año no es divisible por 100
elif year % 100 != 0:
    print("Año Bisiesto")
# Si el año no es divisible por 400
elif year % 400 != 0:
    print("Año Común")
# Si ninguna de las condiciones anteriores se cumple
else:
    print("Año Bisiesto")

income = float(input("Introduce el ingreso anual:"))

# Establecemos un valor predeterminado para el impuesto.
tax = 0.0

# Si el ingreso es positivo, entonces calculamos el impuesto.
if income > 0:
    # Si el ingreso no es superior a 85,528 pesos.
    if income <= 85528:
        tax = (18/100 * income) - 556.02
    # Si el ingreso es superior a 85,528 pesos.
    else:
        tax = 14839.02 + (32/100 * (income - 85528))
    # Si el impuesto es negativo, lo establecemos a cero.
    if tax < 0:
        tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

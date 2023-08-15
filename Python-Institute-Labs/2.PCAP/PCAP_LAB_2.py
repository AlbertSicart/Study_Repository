def display_led(numero):
    # Representación de cada dígito en LED
    representaciones = [
        ['###', '# #', '# #', '# #', '###'],  # 0
        ['  #', '  #', '  #', '  #', '  #'],  # 1
        ['###', '  #', '###', '#  ', '###'],  # 2
        ['###', '  #', '###', '  #', '###'],  # 3
        ['# #', '# #', '###', '  #', '  #'],  # 4
        ['###', '#  ', '###', '  #', '###'],  # 5
        ['###', '#  ', '###', '# #', '###'],  # 6
        ['###', '  #', '  #', '  #', '  #'],  # 7
        ['###', '# #', '###', '# #', '###'],  # 8
        ['###', '# #', '###', '  #', '###']   # 9
    ]

    # Convertir el número a una lista de dígitos
    digitos = list(str(numero))

    # Para cada fila de la representación LED
    for i in range(5):
        # Para cada dígito en el número
        for digito in digitos:
            print(representaciones[int(digito)][i], end=" ")
        print()  # Nueva línea después de completar la fila para todos los dígitos


# Pruebas
numero = input("Ingresa un número: ")
display_led(numero)

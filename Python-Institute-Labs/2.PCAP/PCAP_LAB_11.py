def contar_letras(nombre_archivo):
    # Inicializamos un diccionario para almacenar las ocurrencias de cada letra.
    histograma = {}

    try:
        # Abrimos el archivo en modo lectura.
        with open(nombre_archivo, 'r') as archivo:
            # Leemos todo el contenido del archivo.
            contenido = archivo.read()

            # Recorremos cada letra del contenido.
            for letra in contenido:
                # Convertimos la letra a minúsculas para tratar mayúsculas y minúsculas de igual manera.
                letra = letra.lower()

                # Verificamos si la letra es alfabética.
                if letra.isalpha():
                    # Si la letra ya existe en el diccionario, aumentamos su contador.
                    if letra in histograma:
                        histograma[letra] += 1
                    # Si no, añadimos la letra al diccionario con un contador de 1.
                    else:
                        histograma[letra] = 1

        # Ordenamos el diccionario por sus claves (las letras) y mostramos el histograma.
        for letra, ocurrencias in sorted(histograma.items()):
            if ocurrencias > 0:
                print(f"{letra} -> {ocurrencias}")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")

if __name__ == "__main__":
    # Preguntamos al usuario por el nombre del archivo.
    nombre_archivo = input("Por favor, ingrese el nombre del archivo de entrada: ")
    contar_letras(nombre_archivo)

class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, texto):
        self.msg = f"Línea incorrecta en el archivo: {texto}"

class FileEmpty(StudentsDataException):
    def __init__(self):
        self.msg = "El archivo está vacío."

def leer_archivo_y_sumar_puntos(nombre_archivo):
    estudiantes = {}

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()

            if not contenido:
                raise FileEmpty()

            for linea in contenido:
                datos = linea.split()

                # Verificar si la línea tiene exactamente 3 partes.
                if len(datos) != 3:
                    raise WrongLine(linea.strip())

                nombre, apellido, puntos = datos[0], datos[1], datos[2]

                # Verificar si los puntos son un número.
                try:
                    puntos = float(puntos)
                except ValueError:
                    raise WrongLine(linea.strip())

                # Sumar puntos al estudiante.
                llave = f"{nombre} {apellido}"
                if llave in estudiantes:
                    estudiantes[llave] += puntos
                else:
                    estudiantes[llave] = puntos

        # Ordenar y mostrar resultados.
        estudiantes_ordenados = sorted(estudiantes.items(), key=lambda item: item[0])
        for nombre, puntos in estudiantes_ordenados:
            print(f"{nombre} \t {puntos}")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except StudentsDataException as e:
        print(e.msg)

if __name__ == "__main__":
    # Preguntamos al usuario por el nombre del archivo.
    nombre_archivo = input("Por favor, ingrese el nombre del archivo del profesor Jekyll: ")
    leer_archivo_y_sumar_puntos(nombre_archivo)

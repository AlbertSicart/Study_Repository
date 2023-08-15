import os

def find(path, dir):
    # Utilizar os.walk para navegar por los directorios y subdirectorios
    for dirpath, dirnames, filenames in os.walk(path):
        # Verificar si el nombre del directorio coincide con el nombre que estamos buscando
        if dir in dirnames:
            # Mostrar la ruta absoluta del directorio
            print(os.path.abspath(os.path.join(dirpath, dir)))

if __name__ == "__main__":
    path = input("Introduzca la ruta del directorio donde comenzar la búsqueda (ejemplo: ./tree): ")
    dir = input("Introduzca el nombre del directorio que desea encontrar: ")
    
    find(path, dir)

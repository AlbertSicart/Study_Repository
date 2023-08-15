def mysplit(strng):
    if strng == "":
        return []

    strng = strng.strip()  # Elimina espacios en blanco al inicio y al final de la cadena
    palabra = ""
    lista = []

    for char in strng:
        if char != " ":  # Si el caracter no es un espacio, se agrega a la palabra actual
            palabra += char
        else:
            if palabra:  # Si hay una palabra construida, la añade a la lista
                lista.append(palabra)
                palabra = ""  # Reinicia la palabra
    if palabra:  # Añade la última palabra si existe
        lista.append(palabra)

    return lista

# Pruebas
print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

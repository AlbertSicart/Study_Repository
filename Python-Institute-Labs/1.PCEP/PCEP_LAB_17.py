# Indicar al usuario que ingrese una palabra
user_word = input("Por favor, ingrese una palabra: ")

# Convertir la palabra ingresada a mayúsculas
user_word = user_word.upper()

for letter in user_word:
    # Si la letra es una vocal, usa 'continue' para omitirla
    if letter in ["A", "E", "I", "O", "U"]:
        continue
    print(letter)

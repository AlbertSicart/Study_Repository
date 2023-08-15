blocks = int(input("Ingresa el número de bloques: "))

height = 0
blocks_in_layer = 1

while blocks >= blocks_in_layer:
    height += 1
    blocks -= blocks_in_layer
    blocks_in_layer += 1

print("La altura de la pirámide es:", height)

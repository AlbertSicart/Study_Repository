from datetime import datetime

# Crear el objeto datetime para el 4 de noviembre de 2020, 14:53:00
dt = datetime(2020, 11, 4, 14, 53, 0)

# Imprimir las fechas y tiempos formateados según las especificaciones
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print("Día de la semana:", dt.strftime("%w"))
print("Día del año:", dt.strftime("%j"))
print("Número de semana en el año:", dt.strftime("%U"))

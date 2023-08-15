hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Calculamos el total de minutos.
total_mins = mins + dura

# Calculamos las horas y minutos finales.
final_hour = (hour + total_mins // 60) % 24  # Usamos % 24 para asegurarnos de que las horas estén entre 0 y 23.
final_mins = total_mins % 60  # Usamos % 60 para obtener los minutos restantes.

print(f"{final_hour}:{final_mins}")

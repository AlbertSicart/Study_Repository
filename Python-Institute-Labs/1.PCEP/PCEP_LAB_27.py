def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100 / 1609.344  # Convertir 100 km a millas
    gallon = 3.785411784  # Litros en un galón
    return miles_per_100km / (liters / gallon)

def miles_gallon_to_liters_100km(miles):
    km_per_mile = 1609.344 / 100  # Convertir millas a 100 km
    gallon = 3.785411784  # Litros en un galón
    return 100 / (miles * km_per_mile / gallon)

# Pruebas
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

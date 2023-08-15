def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return days[month - 1]

def day_of_year(year, month, day):
    # Validamos que el día sea válido para el mes dado.
    if day < 1 or day > days_in_month(year, month):
        return None
    
    total_days = sum(days_in_month(year, m) for m in range(1, month)) + day
    return total_days


print(day_of_year(2000, 12, 31))  # Esto debería devolver 366, ya que el año 2000 es bisiesto.

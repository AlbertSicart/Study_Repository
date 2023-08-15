import calendar

class MyCalendar(calendar.Calendar):

    def count_weekday_in_year(self, year, weekday):
        # Inicializar contador
        count = 0

        # Recorrer cada mes del año
        for month in range(1, 13):  # Los meses en Python van de 1 (enero) a 12 (diciembre)
            # monthdays2calendar retorna una lista de semanas, y cada semana es una lista de días (día, día de la semana)
            for week in self.monthdays2calendar(year, month):
                for day, day_week in week:
                    if day != 0 and day_week == weekday:  # Si el día no es 0 (que representa días fuera del mes) y el día de la semana coincide con el solicitado
                        count += 1
        return count


# Pruebas
cal = MyCalendar()

print(cal.count_weekday_in_year(2019, 0))  # Debe imprimir 52
print(cal.count_weekday_in_year(2000, 6))  # Debe imprimir 53

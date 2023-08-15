class WeekDayError(Exception):
    pass


class Weeker:
    __days = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError
        self.__current_day = day

    def __str__(self):
        return self.__current_day

    def add_days(self, n):
        index = (self.__days.index(self.__current_day) + n) % 7
        self.__current_day = self.__days[index]

    def subtract_days(self, n):
        index = (self.__days.index(self.__current_day) - n) % 7
        self.__current_day = self.__days[index]


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lu')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")

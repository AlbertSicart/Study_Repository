import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        # Definir las propiedades privadas para almacenar las coordenadas x e y.
        self.__x = x
        self.__y = y

    def getx(self):
        # Devolver el valor de x.
        return self.__x

    def gety(self):
        # Devolver el valor de y.
        return self.__y

    def distance_from_xy(self, x, y):
        # Calcular y devolver la distancia usando la función hypot.
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        # Calcular y devolver la distancia usando otro objeto Point.
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


# Prueba del código.
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

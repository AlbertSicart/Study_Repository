import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        # Usamos la función distance_from_point de la clase Point para calcular la distancia entre los puntos
        return (self.__vertices[0].distance_from_point(self.__vertices[1]) +
                self.__vertices[1].distance_from_point(self.__vertices[2]) +
                self.__vertices[2].distance_from_point(self.__vertices[0]))

# Probando el código
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())  # Debería imprimir 3.414213562373095

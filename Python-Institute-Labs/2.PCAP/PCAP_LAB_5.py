class QueueError(Exception):  # La nueva excepción se derivará de la clase base Exception.
    def __init__(self, mensaje="Error de Cola"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Queue:
    def __init__(self):
        self.__cola = []

    def put(self, elem):
        self.__cola.append(elem)  # Añadir al final de la lista.

    def get(self):
        if len(self.__cola) == 0:
            raise QueueError  # Lanzar una excepción si la cola está vacía.
        return self.__cola.pop(0)  # Eliminar y devolver el primer elemento de la lista.

que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Error de Cola")

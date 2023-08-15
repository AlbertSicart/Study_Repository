class QueueError(Exception):
    def __init__(self, mensaje="Error de Cola"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Queue:
    def __init__(self):
        self.__cola = []

    def put(self, elem):
        self.__cola.append(elem)

    def get(self):
        if len(self.__cola) == 0:
            raise QueueError
        return self.__cola.pop(0)

class SuperQueue(Queue):
    def isempty(self):
        return len(self.__cola) == 0

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")

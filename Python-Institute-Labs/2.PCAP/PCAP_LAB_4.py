class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        # Inicializa la clase base
        Stack.__init__(self)
        # Inicializa el contador a cero
        self.__counter = 0

    def get_counter(self):
        # Devuelve el valor actual del contador
        return self.__counter

    def pop(self):
        # Incrementa el contador
        self.__counter += 1
        # Llama al método pop de la clase base (la clase Stack)
        return Stack.pop(self)

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())  # Debería imprimir 100

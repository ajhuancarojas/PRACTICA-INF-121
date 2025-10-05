from multipledispatch import dispatch
class Celular:
    def __init__(self, nroTel="", dueño="", espacio=0.0, ram=0, nroApp=0):
        self.__nroTel = nroTel
        self.__dueño = dueño
        self.__espacio = espacio
        self.__ram = ram
        self.__nroApp = nroApp

    @dispatch(int)
    def __add__(self, valor):
        self.__nroApp += 10 * valor
        print(f"Se incrementó el número de Apps en {10 * valor}")
        return self
    @dispatch(int)
    def __sub__(self, valor):
        decremento = 5 * valor
        if self.__espacio >= decremento:
            self.__espacio -= decremento
            print(f"Disminuyó el espacio en {decremento} GB")
        else:
            print("No hay suficiente espacio para disminuir")
        return self

    def mostrarDatos(self):
        print(f"Número cell: {self.__nroTel}")
        print(f"Dueño: {self.__dueño}")
        print(f"Espacio (GB): {self.__espacio}")
        print(f"RAM (GB): {self.__ram}")
        print(f"N° de Apps: {self.__nroApp}\n")

c = Celular("123456789", "ANA CASTRO", 64.0, 9, 8)
print("DATOS ANTES DE LOS OPERADORES:")
c.mostrarDatos()
print("APLICANDO OPERADOR ++:")
c + 1
c.mostrarDatos()
print("APLICANDO OPERADOR -- :")
c - 1  # Disminuye espacio en 5
c.mostrarDatos()
print("RESULTADO FINAL:")
c.mostrarDatos()

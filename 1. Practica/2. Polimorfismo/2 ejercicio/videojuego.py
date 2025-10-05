from multipledispatch import dispatch

class Videojuego:
    def __init__(self, nombre="desconocido", plataforma="desconocida"):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = 0
    @dispatch()
    def agregarJugadores(self):
        self.cantidadJugadores += 1
        print(f"Nuevo jugador total: {self.cantidadJugadores}")
    @dispatch(int)
    def agregarJugadores(self, cantidad):
        if cantidad > 0:
            self.cantidadJugadores += cantidad
            print(f"Se agregaron {cantidad}, total: {self.cantidadJugadores}")
        else:
            print("Error: cantidad inválida")
    @dispatch(object)
    def agregarJugadores(self, scanner):
        cantidad = int(input("Cantidad de jugadores a agregar: "))
        self.agregarJugadores(cantidad)

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Cantidad de jugadores: {self.cantidadJugadores}")

j1 = Videojuego()
j2 = Videojuego("FIFA 2025")
j3 = Videojuego("tarza", "play")
j1.agregarJugadores()
j2.agregarJugadores(3)
j1.mostrarDatos()
j2.mostrarDatos()
j3.mostrarDatos()

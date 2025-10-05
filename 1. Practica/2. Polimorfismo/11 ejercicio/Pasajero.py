from multipledispatch import dispatch

class Pasajero:
    def __init__(self, nombre="", edad=0, genero="", nro_habitacion=0, costo_pasaje=0.0):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nro_habitacion = nro_habitacion
        self.costo_pasaje = costo_pasaje

    @dispatch()
    def __iadd__(self, other=None):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.genero = input("Género (M/F): ")
        self.nro_habitacion = int(input("Nro Habitación: "))
        self.costo_pasaje = float(input("Costo Pasaje: "))
        return self

    @dispatch()
    def __isub__(self, other=None):
        print(f"Pasajero: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, "
              f"Habitación: {self.nro_habitacion}, Costo: {self.costo_pasaje}")
        return self

class Crucero:
    def __init__(self, nombre="", pais_origen="", pais_destino=""):
        self.nombre = nombre
        self.pais_origen = pais_origen
        self.pais_destino = pais_destino
        self.pasajeros = []

    @dispatch(Pasajero)
    def __iadd__(self, pasajero):
        self.pasajeros.append(pasajero)
        return self

    @dispatch()
    def __isub__(self, other=None):
        hombres = sum(1 for p in self.pasajeros if p.genero.upper() == "M")
        mujeres = sum(1 for p in self.pasajeros if p.genero.upper() == "F")
        print(f"Crucero: {self.nombre} -> Hombres: {hombres}, Mujeres: {mujeres}")
        return self
    @dispatch()
    def __eq__(self, other=None):
        total = sum(p.costo_pasaje for p in self.pasajeros)
        print(f"Crucero: {self.nombre} -> Suma total del costo de los pasajes: {total}")
        return total
    @dispatch(object)
    def __add__(self, otro):
        if isinstance(otro, Crucero):
            misma_cantidad = len(self.pasajeros) == len(otro.pasajeros)
            print(f"Crucero {self.nombre} y Crucero {otro.nombre} "
                  f"{'tienen' if misma_cantidad else 'no tienen'} la misma cantidad de pasajeros.")
            return misma_cantidad
        return NotImplemented
    def mostrar(self):
        print(f"\nCrucero: {self.nombre} ({self.pais_origen} → {self.pais_destino})")
        for p in self.pasajeros:
            p -= None

p1 = Pasajero("Juan", 30, "M", 101, 500)
p2 = Pasajero("Ana", 25, "F", 102, 600)
p3 = Pasajero("Luis", 40, "M", 103, 550)
p4 = Pasajero("Maria", 28, "F", 104, 650)
p5 = Pasajero("Carlos", 35, "M", 105, 700)

crucero1 = Crucero("BETTY", "Bolivia", "Brasil")
crucero2 = Crucero("CARLO", "Francia", "Mexico")

crucero1 += p1
crucero1 += p2
crucero1 += p3

crucero2 += p4
crucero2 += p5
crucero1.mostrar()
crucero2.mostrar()
crucero1 == None
crucero2 == None
crucero1 + crucero2
crucero1 -= None
crucero2 -= None

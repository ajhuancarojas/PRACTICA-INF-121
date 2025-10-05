class Vehiculo:
    def __init__(self, conductor, placa, id):
        self.conductor = conductor
        self.placa = placa
        self.id = id

    def mostrar_datos(self):
        print(f"Conductor: {self.conductor}")
        print(f"Placa: {self.placa}")
        print(f"ID: {self.id}")

    def cambiar_conductor(self, nuevo_conductor):
        antiguo_conductor = self.conductor
        self.conductor = nuevo_conductor
        print(f"Conductor cambiado: {antiguo_conductor} -> {nuevo_conductor}")


class Bus(Vehiculo):
    def __init__(self, conductor, placa, id, capacidad, sindicato):
        super().__init__(conductor, placa, id)
        self.capacidad = capacidad
        self.sindicato = sindicato

    def mostrar_datos(self):
        print("\n" + "=" * 30)
        print("DATOS DEL BUS")
        print("=" * 30)
        super().mostrar_datos()
        print(f"Capacidad: {self.capacidad} pasajeros")
        print(f"Sindicato: {self.sindicato}")


class Auto(Vehiculo):
    def __init__(self, conductor, placa, id, caballosFuerza, descapotable):
        super().__init__(conductor, placa, id)
        self.caballosFuerza = caballosFuerza
        self.descapotable = descapotable

    def mostrar_datos(self):
        print("\n" + "=" * 30)
        print("DATOS DEL AUTO")
        print("=" * 30)
        super().mostrar_datos()
        print(f"Caballos de Fuerza: {self.caballosFuerza} HP")
        print(f"Descapotable: {'Sí' if self.descapotable else 'No'}")


class Moto(Vehiculo):
    def __init__(self, conductor, placa, id, cilindrada, casco):
        super().__init__(conductor, placa, id)
        self.cilindrada = cilindrada
        self.casco = casco

    def mostrar_datos(self):
        print("\n" + "=" * 30)
        print("DATOS DE LA MOTO")
        print("=" * 30)
        super().mostrar_datos()
        print(f"Cilindrada: {self.cilindrada} cc")
        print(f"Casco incluido: {'Sí' if self.casco else 'No'}")


print("= VEHICULOS =\n")

bus = Bus("Juan Carlos", "ABC-123", 1, 50, "Sindicato de Transporte Urbano")
auto = Auto("Maria Teresa", "DEF-456", 2, 180, True)
moto = Moto("Pedro Alfonso", "GHI-789", 3, 250, True)

vehiculos = [bus, auto, moto]
for vehiculo in vehiculos:
    vehiculo.mostrar_datos()

print("\n" + "=" * 50)
print("CAMBIANDO CONDUCTORES")
print("=" * 50)

bus.cambiar_conductor("Luis Fernando")
auto.cambiar_conductor("Ana Patricia")

print("\n" + "=" * 50)
print("DATOS ACTUALIZADOS")
print("=" * 50)

for vehiculo in vehiculos:
    vehiculo.mostrar_datos()

print("\n" + "=" * 50)
print("RESUMEN - PLACAS Y CONDUCTORES")
print("=" * 50)

for vehiculo in vehiculos:
    tipo = type(vehiculo).__name__
    print(f"{tipo}: Placa {vehiculo.placa} -> Conductor: {vehiculo.conductor}")
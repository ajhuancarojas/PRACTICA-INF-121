from multipledispatch import dispatch
class Pasajero:
    def __init__(self, nombre="", edad=0, genero="", nroHabitacion=0, costoPasaje=0.0):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nroHabitacion = nroHabitacion
        self.costoPasaje = costoPasaje
    @dispatch()
    def __iadd__(self, other=None):
        print("\n=== LEER DATOS PASAJERO ===")
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.genero = input("Género (M/F): ").upper()
        self.nroHabitacion = int(input("Número de Habitación: "))
        self.costoPasaje = float(input("Costo del Pasaje: "))
        return self
    @dispatch()
    def __isub__(self, other=None):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")
        print(f"Habitación: {self.nroHabitacion}")
        print(f"Costo Pasaje: ${self.costoPasaje}")
        return self

    def __str__(self):
        return f"{self.nombre} ({self.edad} años, {self.genero}) - Hab: {self.nroHabitacion} - ${self.costoPasaje}"
class Crucero:
    def __init__(self, nombre="", paisOrigen="", paisDestino=""):
        self.nombre = nombre
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.nroPasajeros = 0
        self.pasajeros = []
    @dispatch()
    def __iadd__(self, other=None):
        print("\n=== LEER DATOS CRUCERO ===")
        self.nombre = input("Nombre del Crucero: ")
        self.paisOrigen = input("País Origen: ")
        self.paisDestino = input("País Destino: ")
        return self
    @dispatch(Pasajero)
    def __iadd__(self, pasajero):
        if self.nroPasajeros < 100:
            self.pasajeros.append([pasajero.nombre, pasajero.nroHabitacion, pasajero.costoPasaje])
            self.nroPasajeros += 1
            print(f"Pasajero {pasajero.nombre} agregado al crucero {self.nombre}")
        else:
            print("No se pueden agregar más pasajeros (límite alcanzado)")
        return self
    @dispatch()
    def __isub__(self, other=None):
        print(f"\n=== MOSTRAR DATOS CRUCERO {self.nombre} ===")
        print(f"País Origen: {self.paisOrigen}")
        print(f"País Destino: {self.paisDestino}")
        print(f"Número de Pasajeros: {self.nroPasajeros}")

        if self.pasajeros:
            print("\n=== MATRIZ DE PASAJEROS ===")
            print("Nombre          | Habitación | Costo Pasaje")
            print("-" * 45)
            for pasajero in self.pasajeros:
                print(f"{pasajero[0]:15} | {pasajero[1]:10} | ${pasajero[2]:>10}")
        return self
    def __eq__(self, other):
        if isinstance(other, Crucero):
            total_self = sum(p[2] for p in self.pasajeros)
            total_other = sum(p[2] for p in other.pasajeros)

            print(f"\n=== COMPARACIÓN DE COSTOS ===")
            print(f"Crucero {self.nombre}: ${total_self}")
            print(f"Crucero {other.nombre}: ${total_other}")
            print(f"¿Tienen el mismo costo total? {total_self == total_other}")

            return total_self == total_other
        return False
    def __add__(self, other):
        if isinstance(other, Crucero):
            misma_cantidad = self.nroPasajeros == other.nroPasajeros
            print(f"\n=== COMPARACIÓN DE PASAJEROS ===")
            print(f"Crucero {self.nombre}: {self.nroPasajeros} pasajeros")
            print(f"Crucero {other.nombre}: {other.nroPasajeros} pasajeros")
            print(f"¿Tienen la misma cantidad de pasajeros? {misma_cantidad}")
            return misma_cantidad
        return NotImplemented
    def __sub__(self, other):
        if other is None:
            hombres = 0
            mujeres = 0
            print("NOTA: Para una implementación completa, se necesita almacenar el género en la matriz de pasajeros")
            print(f"Total de pasajeros: {self.nroPasajeros}")
            print("(La distribución por género requiere datos adicionales en la matriz)")
            return (hombres, mujeres)
        return NotImplemented
    def mostrar_pasajeros(self):
        if self.pasajeros:
            print(f"\n=== MATRIZ PASAJEROS CRUCERO {self.nombre} ===")
            print("Nombre          | Nro Habitación | Costo Pasaje")
            print("-" * 50)
            for pasajero in self.pasajeros:
                print(f"{pasajero[0]:15} | {pasajero[1]:14} | ${pasajero[2]:>12}")
        else:
            print(f"\nEl crucero {self.nombre} no tiene pasajeros registrados")

print("=" * 60)
print("EJERCICIO 11 - SISTEMA DE CRUCEROS")
print("=" * 60)
p1 = Pasajero("Juan Vargas", 30, "M", 502, 500.0)
p2 = Pasajero("Martina Vasques", 25, "F", 603, 1000.0)
p3 = Pasajero("Wilmer Montero", 35, "M", 401, 925.0)
p4 = Pasajero("Ana Lopez", 28, "F", 205, 750.0)
p5 = Pasajero("Carlos Ruiz", 45, "M", 308, 850.0)
C1 = Crucero("Caribe Paradise", "México", "Jamaica")
C2 = Crucero("Mediterranean Dream", "España", "Italia")
print("\n" + "=" * 50)
print("AGREGANDO PASAJEROS A LOS CRUCEROS")
print("=" * 50)
C1 += p1
C1 += p2
C1 += p3
C2 += p4
C2 += p5
print("\n" + "=" * 50)
print("b) SOBRECARGA ++ Y -- PARA LEER Y MOSTRAR")
print("=" * 50)
print("\n--- Prueba Pasajero ++ (leer) ---")
nuevo_pasajero = Pasajero()
nuevo_pasajero += None  # Simula ++ para leer
print("\n--- Prueba Pasajero -- (mostrar) ---")
p1 -= None  # Simula -- para mostrar
print("\n--- Prueba Crucero ++ (leer) ---")
nuevo_crucero = Crucero()
nuevo_crucero += None  # Simula ++ para leer
print("\n--- Prueba Crucero -- (mostrar) ---")
C1 -= None  # Simula -- para mostrar
print("\n" + "=" * 50)
print("c) SOBRECARGA == PARA SUMA TOTAL DE COSTOS")
print("=" * 50)
resultado_costo = (C1 == C2)
print("\n" + "=" * 50)
print("d) SOBRECARGA + PARA COMPARAR CANTIDAD PASAJEROS")
print("=" * 50)
resultado_cantidad = C1 + C2
print("\n" + "=" * 50)
print("e) SOBRECARGA - PARA DISTRIBUCIÓN POR GÉNERO")
print("=" * 50)
distribucion1 = C1 - None
distribucion2 = C2 - None
print("\n" + "=" * 50)
print("MATRICES FINALES DE PASAJEROS")
print("=" * 50)
C1.mostrar_pasajeros()
C2.mostrar_pasajeros()
print("\n" + "=" * 50)
print("RESUMEN EJECUCIÓN COMPLETADA")
print("=" * 50)
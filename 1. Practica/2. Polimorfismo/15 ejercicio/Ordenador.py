from multipledispatch import dispatch
class Ordenador:
    def __init__(self, codigoSerial="", numero=0, ram=0, procesador="", estado=True):
        self.codigoSerial = codigoSerial
        self.numero = numero
        self.ram = ram
        self.procesador = procesador
        self.estado = estado

    def getCodigoSerial(self):
        return self.codigoSerial
    def getRam(self):
        return self.ram
    def getEstado(self):
        return self.estado
    def setEstado(self, estado):
        self.estado = estado

    def __str__(self):
        estado_str = "Activo" if self.estado else "Inactivo"
        return f"PC#{self.numero} [{self.codigoSerial}] - RAM: {self.ram}GB - {self.procesador} - {estado_str}"
class Laboratorio:
    def __init__(self, nombre="", capacidad=0):
        self.nombre = nombre
        self.capacidad = capacidad
        self.cantidadOrdenadores = 0
        self.ordenadores = []

    def agregarOrdenador(self, ordenador):
        if self.cantidadOrdenadores < self.capacidad:
            self.ordenadores.append(ordenador)
            self.cantidadOrdenadores += 1
            return True
        return False
    @dispatch()
    def informacion(self):
        print(f"\n=== INFORMACIÓN COMPLETA - {self.nombre} ===")
        print(f"Capacidad: {self.capacidad} - Ordenadores: {self.cantidadOrdenadores}")
        if self.ordenadores:
            for ordenador in self.ordenadores:
                print(f"  - {ordenador}")
        else:
            print("  No hay ordenadores en este laboratorio")

    @dispatch(bool)
    def informacion(self, e):
        e_str = "ACTIVOS" if e else "INACTIVOS"
        print(f"\n=== ORDENADORES {e} - {self.nombre} ===")
        encontrados = False
        for ordenador in self.ordenadores:
            if ordenador.getEstado() == e:
                print(f"  - {ordenador}")
                encontrados = True
        if not encontrados:
            print(f"  No hay ordenadores {e_str.lower()}")
    @dispatch(object)
    def informacion(self, l):
        """Mostrar ordenadores que pertenecen a un laboratorio dado"""
        if not isinstance(l, Laboratorio):
            print("Error: El parámetro debe ser un objeto Laboratorio")
            return

        print(f"\n ORDENADORES DEL LABORATORIO {l.nombre} ")
        if l.ordenadores:
            for ordenador in l.ordenadores:
                print(f"  - {ordenador}")
        else:
            print("  El laboratorio no tiene ordenadores")
    @dispatch(int)
    def informacion(self, ramMinima):
        print(f"\n ORDENADORES CON MÁS DE {ramMinima}GB RAM - {self.nombre} ")
        encontrados = False
        for ordenador in self.ordenadores:
            if ordenador.getRam() > ramMinima:
                print(f"  - {ordenador}")
                encontrados = True
        if not encontrados:
            print(f"  No hay ordenadores con más de {ramMinima}GB de RAM")
    def trasladarOrdenadores(self, destino, cantidad=2):
        if not isinstance(destino, Laboratorio):
            print("Error: El destino debe ser un objeto Laboratorio")
            return

        print(f"\n{'=' * 60}")
        print(f"TRASLADO DE ORDENADORES: {self.nombre} → {destino.nombre}")
        print(f"{'=' * 60}")

        print("\n--- ESTADO ANTES DEL TRASLADO ---")
        print(f"{self.nombre}: {self.cantidadOrdenadores} ordenadores")
        print(f"{destino.nombre}: {destino.cantidadOrdenadores} ordenadores")
        if self.cantidadOrdenadores < cantidad:
            print(f"\nError: No hay suficientes ordenadores en {self.nombre}")
            print(f"Solicitados: {cantidad}, Disponibles: {self.cantidadOrdenadores}")
            return
        if destino.cantidadOrdenadores + cantidad > destino.capacidad:
            print(f"\nError: No hay capacidad en {destino.nombre}")
            print(f"Capacidad: {destino.capacidad}, Ocupados: {destino.cantidadOrdenadores}")
            print(
                f"Espacio necesario: {cantidad}, Espacio disponible: {destino.capacidad - destino.cantidadOrdenadores}")
            return
        ordenadores_trasladados = []
        for i in range(min(cantidad, len(self.ordenadores))):
            ordenador = self.ordenadores.pop(0)
            if destino.agregarOrdenador(ordenador):
                ordenadores_trasladados.append(ordenador)
                self.cantidadOrdenadores -= 1

        print(f"\n--- ORDENADORES TRASLADADOS ({len(ordenadores_trasladados)}) ---")
        for ordenador in ordenadores_trasladados:
            print(f"  - {ordenador.getCodigoSerial()} (PC#{ordenador.numero})")
        print("\n--- ESTADO DESPUES DEL TRASLADO ---")
        print(f"{self.nombre}: {self.cantidadOrdenadores} ordenadores")
        print(f"{destino.nombre}: {destino.cantidadOrdenadores} ordenadores")
        print(f"Traslado completado: {len(ordenadores_trasladados)} ordenadores movidos")
    def __str__(self):
        return f"Laboratorio {self.nombre} - Capacidad: {self.capacidad} - Ordenadores: {self.cantidadOrdenadores}"

print("=" * 70)
print("SISTEMA DE GESTIÓN - LABORATORIOS LASIN")
print("=" * 70)
lasin1 = Laboratorio("Lasin 1", 10)
lasin2 = Laboratorio("Lasin 2", 8)
ordenadores = [
    Ordenador("LASIN-PC-001", 1, 16, "Intel i7-10700K", True),
    Ordenador("LASIN-PC-002", 2, 8, "Intel i5-10400", True),
    Ordenador("LASIN-PC-003", 3, 32, "AMD Ryzen 7 5800X", False),
    Ordenador("LASIN-PC-004", 4, 16, "Intel i7-10700", True),
    Ordenador("LASIN-PC-005", 5, 4, "Intel i3-10100", True),
    Ordenador("LASIN-PC-006", 6, 8, "AMD Ryzen 5 3600", False)
    ]

print("\n" + "=" * 50)
print("CONFIGURACIÓN INICIAL DE LABORATORIOS")
print("=" * 50)

for ordenador in ordenadores:
    if lasin1.agregarOrdenador(ordenador):
        print(f"Ordenador {ordenador.codigoSerial} agregado a {lasin1.nombre}")
    else:
        print(f"No se pudo agregar {ordenador.codigoSerial} - Capacidad llena")

print(f"\nEstado inicial:")
print(lasin1)
print(lasin2)
print("\n" + "=" * 50)
print("b) SOBRECARGA DEL MÉTODO INFORMACION")
print("=" * 50)
print("\n1. informacion() - Todos los ordenadores:")
lasin1.informacion()
print("\n2. informacion(True) - Ordenadores activos:")
lasin1.informacion(True)
print("\n3. informacion(False) - Ordenadores inactivos:")
lasin1.informacion(False)
print("\n4. informacion(lasin2) - Ordenadores de Lasin 2:")
lasin1.informacion(lasin2)
print("\n5. informacion(8) - Ordenadores con más de 8GB RAM:")
lasin1.informacion(8)
print("\n" + "=" * 50)
print("c) TRASLADO DE ORDENADORES")
print("=" * 50)
lasin1.trasladarOrdenadores(lasin2, 2)
print("\n" + "=" * 50)
print("ESTADO FINAL DE LOS LABORATORIOS")
print("=" * 50)
print(f"\n{lasin1.nombre}:")
lasin1.informacion()
print(f"\n{lasin2.nombre}:")
lasin2.informacion()
print("\n" + "=" * 50)
print("PRUEBAS ADICIONALES DESPUÉS DEL TRASLADO")
print("=" * 50)
print("\nOrdenadores activos en Lasin 2:")
lasin2.informacion(True)
print("\nOrdenadores con más de 8GB RAM en Lasin 1:")
lasin1.informacion(8)


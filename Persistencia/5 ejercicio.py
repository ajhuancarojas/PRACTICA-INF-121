
import json
import os

class Medicamento:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def to_dict(self):

        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "precio": self.precio
        }

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Bs{self.precio}"

class Sucursal:
    def __init__(self, numero, direccion):
        self.numero = numero
        self.direccion = direccion
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def buscar_medicamentos_tipo(self, tipo):

        return [med for med in self.medicamentos if med.tipo == tipo]

    def buscar_medicamentos_tos(self):

        return self.buscar_medicamentos_tipo("tos")

    def buscar_medicamento_nombre(self, nombre):

        for med in self.medicamentos:
            if med.nombre.lower() == nombre.lower():
                return med
        return None

    def mostrar_medicamentos(self):
        print(f"\nSucursal {self.numero} - {self.direccion}")
        if not self.medicamentos:
            print("  No hay medicamentos")
        for med in self.medicamentos:
            print(f"  - {med}")

    def mover_medicamentos_tipo(self, tipo, sucursal_destino):

        medicamentos_a_mover = []
        medicamentos_a_quedarse = []

        for med in self.medicamentos:
            if med.tipo == tipo:
                medicamentos_a_mover.append(med)
            else:
                medicamentos_a_quedarse.append(med)

        self.medicamentos = medicamentos_a_quedarse
        for med in medicamentos_a_mover:
            sucursal_destino.agregar_medicamento(med)

        return len(medicamentos_a_mover)

    def to_dict(self):

        return {
            "numero": self.numero,
            "direccion": self.direccion,
            "medicamentos": [med.to_dict() for med in self.medicamentos]
        }

    @classmethod
    def from_dict(cls, data):

        sucursal = cls(data["numero"], data["direccion"])
        for med_data in data["medicamentos"]:
            medicamento = Medicamento(
                med_data["nombre"],
                med_data["tipo"],
                med_data["precio"]
            )
            sucursal.medicamentos.append(medicamento)
        return sucursal


class ArchivoFarmacias:
    def __init__(self, nombre_archivo="farmacias.json"):
        self.nombre_archivo = nombre_archivo

    def guardar_sucursal(self, sucursal):

        sucursales = self.cargar_sucursales()


        for i, s in enumerate(sucursales):
            if s.numero == sucursal.numero:
                sucursales[i] = sucursal
                break
        else:
            sucursales.append(sucursal)

        with open(self.nombre_archivo, 'w') as f:
            json.dump([s.to_dict() for s in sucursales], f, indent=2)
        print(f"Sucursal {sucursal.numero} guardada en {self.nombre_archivo}")

    def cargar_sucursales(self):
        if not os.path.exists(self.nombre_archivo):
            return []

        try:
            with open(self.nombre_archivo, 'r') as f:
                data = json.load(f)
            return [Sucursal.from_dict(sucursal_data) for sucursal_data in data]
        except:
            return []

    def buscar_sucursal_por_numero(self, numero):
        sucursales = self.cargar_sucursales()
        for sucursal in sucursales:
            if sucursal.numero == numero:
                return sucursal
        return None

    def buscar_sucursales_con_medicamento(self, nombre_medicamento):

        sucursales = self.cargar_sucursales()
        resultado = []

        for sucursal in sucursales:
            if sucursal.buscar_medicamento_nombre(nombre_medicamento):
                resultado.append(sucursal)

        return resultado

    def ordenar_sucursales_por_direccion(self):

        sucursales = self.cargar_sucursales()
        return sorted(sucursales, key=lambda s: s.direccion)



archivo = ArchivoFarmacias()

sucursal1 = Sucursal(101, "Av. Libertador 123")
sucursal1.agregar_medicamento(Medicamento("Jarabe para la tos", "tos", 15.50))
sucursal1.agregar_medicamento(Medicamento("Tapsin", "dolor", 8.75))
sucursal1.agregar_medicamento(Medicamento("Antigripal", "gripe", 12.30))

sucursal2 = Sucursal(102, "Calle Principal 456")
sucursal2.agregar_medicamento(Medicamento("Tapsin", "dolor", 8.75))
sucursal2.agregar_medicamento(Medicamento("Aspirina", "dolor", 5.25))
sucursal2.agregar_medicamento(Medicamento("Pastillas para la tos", "tos", 7.80))

archivo.guardar_sucursal(sucursal1)
archivo.guardar_sucursal(sucursal2)


print("\n  Medicamentos para la Gripe en Sucursal 101 ")
sucursal = archivo.buscar_sucursal_por_numero(101)
if sucursal:
    medicamentos_tos = sucursal.buscar_medicamentos_tos()
    if medicamentos_tos:
        for med in medicamentos_tos:
            print(f"  - {med}")
    else:
        print("  No hay medicamentos para la tos")


print("\n  Sucursales con Tapsin ")
sucursales_con_tapsin = archivo.buscar_sucursales_con_medicamento("Tapsin")
for s in sucursales_con_tapsin:
    print(f"  Sucursal {s.numero}: {s.direccion}")


print("\n Buscar medicamentos tipo 'dolor'")
sucursales = archivo.cargar_sucursales()
for sucursal in sucursales:
    medicamentos_dolor = sucursal.buscar_medicamentos_tipo("dolor")
    if medicamentos_dolor:
        print(f"\nSucursal {sucursal.numero}:")
        for med in medicamentos_dolor:
            print(f"  - {med}")

print("\n Farmacias ordenadas por dirección ")
sucursales_ordenadas = archivo.ordenar_sucursales_por_direccion()
for s in sucursales_ordenadas:
    print(f"  {s.direccion} (Sucursal {s.numero})")

print("\n Mover medicamentos de tipo 'tos'")
sucursal_origen = archivo.buscar_sucursal_por_numero(101)
sucursal_destino = archivo.buscar_sucursal_por_numero(102)

if sucursal_origen and sucursal_destino:
    movidos = sucursal_origen.mover_medicamentos_tipo("tos", sucursal_destino)
    print(f"  Se movieron {movidos} medicamentos")

    archivo.guardar_sucursal(sucursal_origen)
    archivo.guardar_sucursal(sucursal_destino)

    print("\n  Estado después del movimiento:")
    sucursal_origen.mostrar_medicamentos()
    sucursal_destino.mostrar_medicamentos()


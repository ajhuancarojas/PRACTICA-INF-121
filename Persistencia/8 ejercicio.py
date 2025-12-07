
import json
import os


class Alimento:
    def __init__(self, nombre, fechaVencimiento, cantidad):
        self.nombre = nombre
        self.fechaVencimiento = fechaVencimiento
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fechaVencimiento": self.fechaVencimiento,
            "cantidad": self.cantidad
        }


class ArchRefri:
    def __init__(self, nombre="refrigerador.json"):
        self.nombre = nombre
    def crear(self):
        if not os.path.exists(self.nombre):
            with open(self.nombre, 'w') as f:
                json.dump([], f)

    def modificar_por_nombre(self, nombre, nuevo_alimento):
        alimentos = self.leer()
        for i, alimento in enumerate(alimentos):
            if alimento.nombre == nombre:
                alimentos[i] = nuevo_alimento
                break
        self.guardar_todos(alimentos)

    def eliminar_por_nombre(self, nombre):
        alimentos = self.leer()
        alimentos = [a for a in alimentos if a.nombre != nombre]
        self.guardar_todos(alimentos)

    def alimentos_caducan_antes(self, fecha):
        alimentos = self.leer()
        resultado = []

        for alimento in alimentos:
            if alimento.fechaVencimiento < fecha:
                resultado.append(alimento)

        print(f"Alimentos que caducan antes de {fecha}:")
        for a in resultado:
            print(f"  {a.nombre} - Vence: {a.fechaVencimiento}")

        return resultado

    def eliminar_cantidad_cero(self):
        alimentos = self.leer()
        alimentos = [a for a in alimentos if a.cantidad > 0]
        self.guardar_todos(alimentos)
        print("Alimentos con cantidad 0 eliminados")

    def buscar_alimentos_vencidos(self):
        alimentos = self.leer()
        hoy = "15/11/2025"

        vencidos = []
        for alimento in alimentos:
            if alimento.fechaVencimiento < hoy:
                vencidos.append(alimento)

        print("Alimentos vencidos:")
        for a in vencidos:
            print(f"  {a.nombre} - Vencido: {a.fechaVencimiento}")

        return vencidos

    def alimento_mas_cantidad(self):
        alimentos = self.leer()

        if not alimentos:
            print("No hay alimentos")
            return None

        mayor = max(alimentos, key=lambda x: x.cantidad)
        print(f"Alimento con más cantidad: {mayor.nombre} - Cantidad: {mayor.cantidad}")
        return mayor

    def leer(self):
        if not os.path.exists(self.nombre):
            return []

        with open(self.nombre, 'r') as f:
            data = json.load(f)

        alimentos = []
        for item in data:
            alimento = Alimento(item["nombre"], item["fechaVencimiento"], item["cantidad"])
            alimentos.append(alimento)

        return alimentos

    def guardar_todos(self, alimentos):
        with open(self.nombre, 'w') as f:
            json.dump([a.to_dict() for a in alimentos], f, indent=2)

archivo = ArchRefri()
archivo.crear()

print("\n=== a) Modificar 'Queso' ===")
nuevo_queso = Alimento("Queso", "15/11/2025", 2)
archivo.modificar_por_nombre("Queso", nuevo_queso)

print("=== a) Eliminar 'Pan' ===")
archivo.eliminar_por_nombre("Pan")

print("\n=== b) Alimentos que caducan antes de 20/11/2025 ===")
archivo.alimentos_caducan_antes("20/11/2025")

print("\n=== c) Eliminar alimentos cantidad 0 ===")
archivo.eliminar_cantidad_cero()

print("\n=== d) Buscar alimentos vencidos (antes de 15/11/2025) ===")
archivo.buscar_alimentos_vencidos()

print("\n=== e) Alimento con más cantidad ===")
archivo.alimento_mas_cantidad()


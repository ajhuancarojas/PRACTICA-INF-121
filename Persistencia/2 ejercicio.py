import json
import os


class Trabajador:
    def __init__(self, nombre, carnet, salario):
        self.nombre = nombre
        self.carnet = carnet
        self.salario = salario

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "carnet": self.carnet,
            "salario": self.salario
        }


class ArchivoTrabajador:
    def __init__(self, nombre_archivo="trabajadores.json"):
        self.nombre_archivo = nombre_archivo

    def crear_archivo(self):
        if not os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, 'w') as f:
                json.dump([], f)

    def guardar_trabajador(self, trabajador):
        trabajadores = self.cargar_trabajadores()
        trabajadores.append(trabajador)
        with open(self.nombre_archivo, 'w') as f:
            json.dump([t.to_dict() for t in trabajadores], f, indent=2)

    def cargar_trabajadores(self):
        if not os.path.exists(self.nombre_archivo):
            return []
        with open(self.nombre_archivo, 'r') as f:
            data = json.load(f)
        return [Trabajador(t["nombre"], t["carnet"], t["salario"]) for t in data]

    def aumentar_salario(self, porcentaje, trabajador):
        trabajador.salario *= (1 + porcentaje / 100)
        # Actualizar en archivo
        trabajadores = self.cargar_trabajadores()
        for i, t in enumerate(trabajadores):
            if t.carnet == trabajador.carnet:
                trabajadores[i] = trabajador
                break
        with open(self.nombre_archivo, 'w') as f:
            json.dump([t.to_dict() for t in trabajadores], f, indent=2)

    def buscar_mayor_salario(self):
        trabajadores = self.cargar_trabajadores()
        if not trabajadores:
            return None
        return max(trabajadores, key=lambda x: x.salario)

    def ordenar_por_salario(self):
        trabajadores = self.cargar_trabajadores()
        return sorted(trabajadores, key=lambda x: x.salario)


archivo = ArchivoTrabajador()
archivo.crear_archivo()
t1 = Trabajador("ANA QUISPE", 1001, 2500.0)
t2 = Trabajador("LUIS VALVERDE", 1002, 3200.0)

archivo.guardar_trabajador(t1)
archivo.guardar_trabajador(t2)

mayor = archivo.buscar_mayor_salario()
print(f"Mayor salario: {mayor.nombre} - Bs {mayor.salario}")
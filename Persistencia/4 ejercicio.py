import json
import os


class Estudiante:
    def __init__(self, ru, nombre, paterno, materno, edad):
        self.ru = ru
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad

    def to_dict(self):
        return {
            "ru": self.ru,
            "nombre": self.nombre,
            "paterno": self.paterno,
            "materno": self.materno,
            "edad": self.edad
        }


class Nota:
    def __init__(self, materia, notaFinal, estudiante):
        self.materia = materia
        self.notaFinal = notaFinal
        self.estudiante = estudiante

    def to_dict(self):
        return {
            "materia": self.materia,
            "notaFinal": self.notaFinal,
            "estudiante": self.estudiante.to_dict()
        }


class ArchivoNota:
    def __init__(self, nombre_archivo="notas.json"):
        self.nombre_archivo = nombre_archivo

    def agregar_estudiantes(self, notas):
        datos = self.cargar_datos()
        datos.extend(notas)
        with open(self.nombre_archivo, 'w') as f:
            json.dump([n.to_dict() for n in datos], f, indent=2)

    def cargar_datos(self):
        if not os.path.exists(self.nombre_archivo):
            return []
        with open(self.nombre_archivo, 'r') as f:
            data = json.load(f)
        notas = []
        for item in data:
            est_data = item["estudiante"]
            estudiante = Estudiante(
                est_data["ru"], est_data["nombre"],
                est_data["paterno"], est_data["materno"],
                est_data["edad"]
            )
            nota = Nota(item["materia"], item["notaFinal"], estudiante)
            notas.append(nota)
        return notas

    def promedio_notas(self):
        notas = self.cargar_datos()
        if not notas:
            return 0
        total = sum(n.notaFinal for n in notas)
        return total / len(notas)

    def mejores_estudiantes(self):
        notas = self.cargar_datos()
        if not notas:
            return []
        max_nota = max(n.notaFinal for n in notas)
        return [n for n in notas if n.notaFinal == max_nota]

    def eliminar_por_materia(self, materia):
        notas = self.cargar_datos()
        notas_filtradas = [n for n in notas if n.materia.lower() != materia.lower()]
        with open(self.nombre_archivo, 'w') as f:
            json.dump([n.to_dict() for n in notas_filtradas], f, indent=2)


archivo = ArchivoNota()

e1 = Estudiante("12345", "Saul", "Pérez", "Gómez", 20)
n1 = Nota("Matemáticas", 80.5, e1)

e2 = Estudiante("67890", "Jilari", "López", "Rodríguez", 21)
n2 = Nota("Física", 92.0, e2)

archivo.agregar_estudiantes([n1, n2])

print(f"Promedio: {archivo.promedio_notas():.2f}")
print(f"Mejores estudiantes: {len(archivo.mejores_estudiantes())}")

import json
import os
class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.ci = ci


class Niño(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci, edad, peso, talla):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, ci)
        self.edad = edad
        self.peso = peso
        self.talla = talla

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellidoPaterno": self.apellidoPaterno,
            "apellidoMaterno": self.apellidoMaterno,
            "ci": self.ci,
            "edad": self.edad,
            "peso": self.peso,
            "talla": self.talla
        }
class ArchivoNiños:
    def __init__(self, nombre_archivo="niños.json"):
        self.nombre_archivo = nombre_archivo
    def crear(self):

        with open(self.nombre_archivo, 'w') as f:
            json.dump([], f)

    def leer(self):

        if not os.path.exists(self.nombre_archivo):
            return []

        with open(self.nombre_archivo, 'r') as f:
            data = json.load(f)

        niños = []
        for item in data:
            niño = Niño(
                item["nombre"],
                item["apellidoPaterno"],
                item["apellidoMaterno"],
                item["ci"],
                item["edad"],
                item["peso"],
                item["talla"]
            )
            niños.append(niño)
        return niños

    def listar(self):
        niños = self.leer()
        for niño in niños:
            print(f"CI: {niño.ci}, Nombre: {niño.nombre} {niño.apellidoPaterno}")

    def mostrar(self, ci):
        niños = self.leer()
        for niño in niños:
            if niño.ci == ci:
                print(f"Nombre: {niño.nombre}")
                print(f"Apellidos: {niño.apellidoPaterno} {niño.apellidoMaterno}")
                print(f"CI: {niño.ci}")
                print(f"Edad: {niño.edad}")
                print(f"Peso: {niño.peso}")
                print(f"Talla: {niño.talla}")
                return
        print("Niño no encontrado")

    def contar_peso_adecuado(self):
        niños = self.leer()
        contador = 0

        for niño in niños:
            try:
                edad_num = int(niño.edad)
                peso_num = float(niño.peso)
                talla_num = float(niño.talla)


                peso_ideal = (talla_num - 100) * 0.9

                if edad_num < 12:
                    peso_ideal = edad_num * 2 + 8

                if abs(peso_num - peso_ideal) <= (peso_ideal * 0.15):
                    contador += 1
            except:
                continue

        print(f"Niños con peso adecuado: {contador}")
        return contador

    def mostrar_inadecuados(self):
        niños = self.leer()

        for niño in niños:
            try:
                edad_num = int(niño.edad)
                peso_num = float(niño.peso)
                talla_num = float(niño.talla)

                talla_ideal = edad_num * 6 + 77
                peso_ideal = edad_num * 2 + 8

                talla_adecuada = abs(talla_num - talla_ideal) <= 10
                peso_adecuado = abs(peso_num - peso_ideal) <= 3

                if not (talla_adecuada and peso_adecuado):
                    print(f"Niño inadecuado: {niño.nombre} {niño.apellidoPaterno}")
                    print(f"  Edad: {edad_num}, Peso actual: {peso_num}, Peso ideal: {peso_ideal:.1f}")
                    print(f"  Talla actual: {talla_num}, Talla ideal: {talla_ideal:.1f}")
                    print()
            except:
                continue

    def promedio_edad(self):
        niños = self.leer()
        if not niños:
            print("Promedio de edad: 0")
            return 0

        total_edad = 0
        contador = 0

        for niño in niños:
            try:
                total_edad += int(niño.edad)
                contador += 1
            except:
                continue

        promedio = total_edad / contador if contador > 0 else 0
        print(f"Promedio de edad: {promedio:.1f}")
        return promedio

    def buscar_por_ci(self, ci):
        niños = self.leer()

        for niño in niños:
            if niño.ci == ci:
                print(f"Niño encontrado: {niño.nombre} {niño.apellidoPaterno}")
                return niño

        print(f"No se encontró niño con CI: {ci}")
        return None

    def mostrar_talla_mas_alta(self):
        niños = self.leer()

        if not niños:
            print("No hay niños registrados")
            return

        max_talla = 0
        for niño in niños:
            try:
                talla = float(niño.talla)
                if talla > max_talla:
                    max_talla = talla
            except:
                continue

        print(f"Talla más alta: {max_talla} cm")
        print("Niños con esta talla:")

        for niño in niños:
            try:
                if float(niño.talla) == max_talla:
                    print(f"- {niño.nombre} {niño.apellidoPaterno}")
            except:
                continue

archivo = ArchivoNiños("niños.json")

if not os.path.exists("niños.json"):
    archivo.crear()

niños_ejemplo = [
    Niño("Juan", "Pérez", "Gómez", 1001, 8, "30", "130"),
    Niño("María", "López", "Rodríguez", 1002, 10, "38", "145"),
    Niño("Carlos", "García", "Fernández", 1003, 7, "25", "125"),
    Niño("Ana", "Martínez", "Sánchez", 1004, 12, "45", "155"),
    Niño("Pedro", "Díaz", "Torres", 1005, 9, "35", "140"),
    Niño("Laura", "Ruiz", "Vargas", 1006, 11, "40", "150")
]
datos_guardar = [n.to_dict() for n in niños_ejemplo]
with open("niños.json", 'w') as f:
    json.dump(datos_guardar, f, indent=2)

print("=" * 50)
print("EJERCICIO 7: PERSONA Y NIÑO")
print("=" * 50)

print("\a) LISTAR todos los niños ")
archivo.listar()

print("\n a) MOSTRAR niño con CI 1003")
archivo.mostrar(1003)

print("\n b) CONTAR niños con peso adecuado")
archivo.contar_peso_adecuado()

print("\n c) MOSTRAR niños con peso/talla inadecuada ")
archivo.mostrar_inadecuados()

print("\n d) PROMEDIO de edad ")
archivo.promedio_edad()

print("\n e) BUSCAR niño por CI (1004) ")
archivo.buscar_por_ci(1004)

print("\n f) MOSTRAR niños con talla más alta ")
archivo.mostrar_talla_mas_alta()

print("\n" + "=" * 50)




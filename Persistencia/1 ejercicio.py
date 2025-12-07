import json
import os


class Charango:
    def __init__(self, material, nroCuerdas):
        self.material = material
        self.nroCuerdas = nroCuerdas
        self.cuerdas = [True] * 10  # Todas las cuerdas en buen estado

    def contar_cuerdas_falsas(self):
        return self.cuerdas.count(False)

    def to_dict(self):
        return {
            "material": self.material,
            "nroCuerdas": self.nroCuerdas,
            "cuerdas": self.cuerdas
        }


class ArchivoCharango:
    def __init__(self, nombre_archivo="charangos.json"):
        self.nombre_archivo = nombre_archivo

    def guardar_charango(self, charango):
        charangos = self.cargar_charangos()
        charangos.append(charango)
        with open(self.nombre_archivo, 'w') as f:
            json.dump([c.to_dict() for c in charangos], f, indent=2)

    def cargar_charangos(self):
        if not os.path.exists(self.nombre_archivo):
            return []
        with open(self.nombre_archivo, 'r') as f:
            data = json.load(f)
        charangos = []
        for item in data:
            c = Charango(item["material"], item["nroCuerdas"])
            c.cuerdas = item["cuerdas"]
            charangos.append(c)
        return charangos

    def eliminar_cuerdas_falsas_mayor_6(self):
        charangos = self.cargar_charangos()
        charangos_filtrados = [c for c in charangos if c.contar_cuerdas_falsas() <= 6]
        with open(self.nombre_archivo, 'w') as f:
            json.dump([c.to_dict() for c in charangos_filtrados], f, indent=2)

    def listar_por_material(self, material):
        charangos = self.cargar_charangos()
        return [c for c in charangos if c.material.lower() == material.lower()]

    def buscar_10_cuerdas(self):
        charangos = self.cargar_charangos()
        return [c for c in charangos if c.nroCuerdas == 10]

    def ordenar_por_material(self):
        charangos = self.cargar_charangos()
        return sorted(charangos, key=lambda x: x.material)



archivo = ArchivoCharango()

c1 = Charango("Madera", 10)
c1.cuerdas = [True, True, False, True, False, False, True, False, False, False]  # 6 falsas
c2 = Charango("Plástico", 8)
c2.cuerdas = [True] * 8 + [False] * 2
c3 = Charango("Madera", 10)
c3.cuerdas = [True] * 4 + [False] * 6

archivo.guardar_charango(c1)
archivo.guardar_charango(c2)
archivo.guardar_charango(c3)

print("Charangos con 10 cuerdas:", len(archivo.buscar_10_cuerdas()))
print("Charangos de madera:", len(archivo.listar_por_material("madera")))
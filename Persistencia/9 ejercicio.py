
import json
import os


class Animal:
    def __init__(self, especie, nombre, cantidad):
        self.especie = especie
        self.nombre = nombre
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "especie": self.especie,
            "nombre": self.nombre,
            "cantidad": self.cantidad
        }


class Zoologico:
    def __init__(self, id_zoo, nombre):
        self.id = id_zoo
        self.nombre = nombre
        self.moAnimales = 0
        self.animales = []

    def agregar_animal(self, animal):
        if len(self.animales) < 30:
            self.animales.append(animal)
            self.moAnimales += animal.cantidad

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "moAnimales": self.moAnimales,
            "animales": [a.to_dict() for a in self.animales]
        }


class ArchZoo:
    def __init__(self, nombre="zoologicos.json"):
        self.nombre = nombre

    def crear(self):
        if not os.path.exists(self.nombre):
            with open(self.nombre, 'w') as f:
                json.dump([], f)

    def modificar(self, id_zoo, nuevo_zoo):
        zoos = self.leer()
        for i, zoo in enumerate(zoos):
            if zoo.id == id_zoo:
                zoos[i] = nuevo_zoo
                break
        self.guardar_todos(zoos)

    def eliminar(self, id_zoo):
        zoos = self.leer()
        zoos = [z for z in zoos if z.id != id_zoo]
        self.guardar_todos(zoos)

    def listar_mayor_variedad(self):
        zoos = self.leer()
        if not zoos:
            return []

        variedades = []
        for zoo in zoos:
            especies = set()
            for animal in zoo.animales:
                especies.add(animal.especie)
            variedades.append((zoo, len(especies)))


        max_variedad = max(variedad[1] for variedad in variedades)
        resultado = [variedad[0] for variedad in variedades if variedad[1] == max_variedad]

        print(f"Zoológicos con mayor variedad ({max_variedad} especies):")
        for zoo in resultado:
            print(f"  {zoo.nombre}")

        return resultado

    def listar_vacios_eliminar(self):
        zoos = self.leer()
        vacios = [zoo for zoo in zoos if zoo.moAnimales == 0]

        print("Zoológicos vacíos (eliminados):")
        for zoo in vacios:
            print(f"  {zoo.nombre}")

        zoos = [zoo for zoo in zoos if zoo.moAnimales > 0]
        self.guardar_todos(zoos)

        return vacios

    def mostrar_animales_especie(self, especie):
        zoos = self.leer()

        print(f"Animales de especie '{especie}':")
        encontrados = False

        for zoo in zoos:
            for animal in zoo.animales:
                if animal.especie == especie:
                    print(f"  {animal.nombre} en {zoo.nombre} - Cantidad: {animal.cantidad}")
                    encontrados = True

        if not encontrados:
            print(f"  No hay animales de especie '{especie}'")

    def mover_animales(self, especie, id_origen, id_destino):
        zoos = self.leer()

        origen = None
        destino = None

        for zoo in zoos:
            if zoo.id == id_origen:
                origen = zoo
            if zoo.id == id_destino:
                destino = zoo

        if not origen or not destino:
            print("Zoológicos no encontrados")
            return

        animales_a_mover = []
        animales_a_quedarse = []

        for animal in origen.animales:
            if animal.especie == especie:
                animales_a_mover.append(animal)
            else:
                animales_a_quedarse.append(animal)

        origen.animales = animales_a_quedarse
        origen.moAnimales = sum(a.cantidad for a in animales_a_quedarse)

        for animal in animales_a_mover:
            destino.agregar_animal(animal)

        self.guardar_todos(zoos)

        print(f"Se movieron {len(animales_a_mover)} animales de especie '{especie}'")
        print(f"  De: {origen.nombre}")
        print(f"  A: {destino.nombre}")

    def leer(self):
        if not os.path.exists(self.nombre):
            return []

        with open(self.nombre, 'r') as f:
            data = json.load(f)

        zoos = []
        for item in data:
            zoo = Zoologico(item["id"], item["nombre"])
            zoo.moAnimales = item["moAnimales"]
            for a in item["animales"]:
                animal = Animal(a["especie"], a["nombre"], a["cantidad"])
                zoo.animales.append(animal)
            zoos.append(zoo)

        return zoos

    def guardar_todos(self, zoos):
        with open(self.nombre, 'w') as f:
            json.dump([z.to_dict() for z in zoos], f, indent=2)


def main():
    archivo = ArchZoo()
    archivo.crear()
    zoo1 = Zoologico(1, "Zoo Central")
    zoo1.agregar_animal(Animal("León", "Simba", 2))
    zoo1.agregar_animal(Animal("Tigre", "Rajah", 1))
    zoo1.agregar_animal(Animal("Elefante", "Dumbo", 3))

    zoo2 = Zoologico(2, "Zoo Norte")
    zoo2.agregar_animal(Animal("León", "Mufasa", 1))
    zoo2.agregar_animal(Animal("Jirafa", "Melman", 2))

    zoo3 = Zoologico(3, "Zoo Sur")  # Vacío

    zoo4 = Zoologico(4, "Zoo Este")
    zoo4.agregar_animal(Animal("León", "Alex", 2))
    zoo4.agregar_animal(Animal("Mono", "George", 5))

    with open("zoologicos.json", 'w') as f:
        json.dump([zoo1.to_dict(), zoo2.to_dict(), zoo3.to_dict(), zoo4.to_dict()], f, indent=2)

    print(" ZOOLÓGICO")
    print("=" * 50)
    print("\n=== a) Modificar Zoo Central ===")
    zoo1_mod = Zoologico(1, "Zoo Central Modificado")
    zoo1_mod.agregar_animal(Animal("León", "Simba Jr", 3))
    archivo.modificar(1, zoo1_mod)

    print("=== a) Eliminar Zoo Sur (vacío) ===")
    archivo.eliminar(3)

    print("\n=== b) Zoológicos con mayor variedad ===")
    archivo.listar_mayor_variedad()

    print("\n=== c) Eliminar zoológicos vacíos ===")
    archivo.listar_vacios_eliminar()

    print("\n=== d) Mostrar animales 'León' ===")
    archivo.mostrar_animales_especie("León")

    print("\n=== e) Mover Leones de Zoo Central a Zoo Norte ===")
    archivo.mover_animales("León", 1, 2)

if __name__ == "__main__":
    main()
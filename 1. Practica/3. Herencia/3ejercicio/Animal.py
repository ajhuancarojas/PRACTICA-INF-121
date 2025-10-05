from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def desplazarse(self):
        pass

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")

class Leon(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print(f"{self.nombre} el leon camina majestuosamente por la sabana.")

class Pinguino(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print(f"{self.nombre} el pinguino se desliza elegantemente sobre el hielo.")

class Canguro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print(f"{self.nombre} el canguro salta poderosamente con sus patas traseras.")


def contar_animales(animales, tipo):
    count = 0
    for animal in animales:
        if type(animal).__name__ == tipo:
            count += 1
    return count

print("=== ZOOLOGICO VIRTUAL ===")
animales = [
    Leon("Simba", 5),
    Pinguino("Pingu", 3),
    Canguro("Jack", 4),
    Leon("Mufasa", 12)
]
for animal in animales:
    print("\n---")
    animal.mostrar_info()
    animal.desplazarse()

print("\n= ZOOLOGICO =")
print(f"Total de animales: {len(animales)}")
print("Tipos de animales:")
print(f" - Leones: {contar_animales(animales, 'Leon')}")
print(f" - Pinguinos: {contar_animales(animales, 'Pinguino')}")
print(f" - Canguros: {contar_animales(animales, 'Canguro')}")


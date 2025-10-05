
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    @abstractmethod
    def desplazarse(self):
        pass
    def mostrar_info(self):
        print(f"Animal: {self.nombre}")
        print(f"Edad: {self.edad} años")
class Leon(Animal):
    def desplazarse(self):
        print(f" {self.nombre} camina por la sabana")
    
    def rugir(self):
        print(f"¡{self.nombre} ruge fuerte!")
class Pinguino(Animal):
    def desplazarse(self):
        print(f" {self.nombre} se desliza sobre el hielo")

    def nadar(self):
        print(f"{self.nombre} nada en el agua fría")
class Canguro(Animal):
    def desplazarse(self):
        print(f" {self.nombre} salta con sus patas")
    def saltar(self):
        print(f"{self.nombre} salta muy alto")

leon = Leon("Simba", 5)
pinguino = Pinguino("Pingu", 3)
canguro = Canguro("Jack", 4)
animales = [leon, pinguino, canguro]
print("1. INFORMACIÓN DE ANIMALES:")
for animal in animales:
    animal.mostrar_info()
    animal.desplazarse()
print("\n2. COMPORTAMIENTOS ESPECIALES:")
leon.rugir()
pinguino.nadar()
canguro.saltar()
for animal in animales:
    print(f"{animal.nombre}: ", end="")
    animal.desplazarse()
print("\n4. ESTADÍSTICAS:")
print(f"Total animales: {len(animales)}")
print(f"Animal más viejo: {max(animales, key=lambda x: x.edad).nombre}")
print("\n5. MODIFICAR:")
leon.nombre = "Simba Adulto"
leon.edad = 6
leon.mostrar_info()
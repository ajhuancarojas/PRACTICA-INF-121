class Politico:
    def __init__(self, profesion, añosExp):
        self.profesion = profesion
        self.añosExp = añosExp

    def mostrar_datos(self):
        print(f"   Profesion: {self.profesion}")
        print(f"   Años de experiencia: {self.añosExp}")

class Partido:
    def __init__(self, nombreP, rol):
        self.nombreP = nombreP
        self.rol = rol

    def mostrar_datos(self):
        print(f"   Partido: {self.nombreP}")
        print(f"   Rol: {self.rol}")

class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, añosExp, nombreP, rol):
        Politico.__init__(self, profesion, añosExp)
        Partido.__init__(self, nombreP, rol)
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_datos(self):
        print(f"\nPRESIDENTE: {self.nombre} {self.apellido}")
        Politico.mostrar_datos(self)
        Partido.mostrar_datos(self)
print("SISTEMA DE PRESIDENTES\n")
print("--- PRIMERA  ---")
presidente1 = Presidente("Luis", "Arce", "Economista", 20, "MAS", "Gobierno")

print("--- SEGUNDA  ---")

presidente2 = Presidente("Jeanine", "Anez", "Comunicadora", 15, "democracia", "oposicion")
presidente3 = Presidente("Evo", "Morales", "Dirigente Sindical", 25, "MAS", "Fundador")
presidentes = [presidente1, presidente2, presidente3]

print("\n LISTA COMPLETA DE PRESIDENTES ")
for i, presi in enumerate(presidentes, 1):
    print(f"\nPresidente {i}:")
    presi.mostrar_datos()
def buscar_presidente_por_nombre(nombre, lista_presidentes):
    for presi in lista_presidentes:
        if presi.nombre.lower() == nombre.lower():
            return presi
    return None
print("BUSQUEDA DE PRESIDENTE")
nombre_buscado = "Luis"
presidente_encontrado = buscar_presidente_por_nombre(nombre_buscado, presidentes)
if presidente_encontrado:
    print(f"Presidente encontrado: {presidente_encontrado.nombre} {presidente_encontrado.apellido}")
    print(f"Partido politico: {presidente_encontrado.nombreP}")
    print(f"Profesion: {presidente_encontrado.profesion}")
else:
    print(f"No se encontro presidente con nombre: {nombre_buscado}")
nombre_buscado2 = "Evo"
presidente_encontrado2 = buscar_presidente_por_nombre(nombre_buscado2, presidentes)
if presidente_encontrado2:
    print(f"Presidente encontrado: {presidente_encontrado2.nombre} {presidente_encontrado2.apellido}")
    print(f"Partido politico: {presidente_encontrado2.nombreP}")
    print(f"Profesion: {presidente_encontrado2.profesion}")
else:
    print(f"No se encontro presidente con nombre: {nombre_buscado2}")
print("INFORMACION DEL SISTEMA")
print(f"Total de presidentes registrados: {len(presidentes)}")
partidos = {}
for presi in presidentes:
    if presi.nombreP in partidos:
        partidos[presi.nombreP] += 1
    else:
        partidos[presi.nombreP] = 1
print("\nPresidentes por partido:")
for partido, cantidad in partidos.items():
    print(f"   {partido}: {cantidad} presidente(s)")
experiencia_promedio = sum(presi.añosExp for presi in presidentes) / len(presidentes)
print(f"\nExperiencia promedio: {experiencia_promedio:.1f} años")
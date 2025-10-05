class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self.nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self._edad = edad  
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Paterno: {self._paterno}")
        print(f"Materno: {self._materno}")
        print(f"Edad: {self._edad}")


class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, regProfesional):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.regProfesional = regProfesional

    def mostrar(self):
        print("\n" + "=" * 30)
        print("DATOS DEL DOCENTE")
        print("=" * 30)
        super().mostrar()
        print(f"Sueldo: {self.sueldo}")
        print(f"Registro Profesional: {self.regProfesional}")


class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula

    def mostrar(self):
        print("\n" + "=" * 30)
        print("DATOS DEL ESTUDIANTE")
        print("=" * 30)
        super().mostrar()
        print(f"RU: {self.ru}")
        print(f"Matricula: {self.matricula}")

    def modificarEdad(self, nueva_edad):
        if nueva_edad >= 0:
            edad_anterior = self._edad
            self._edad = nueva_edad
            print(f"Edad modificada: {edad_anterior} -> {self._edad}")
        else:
            print("Error: La edad no puede ser negativa")
def promedio(estudiantes):
    if not estudiantes:
        return 0
    total = sum(estudiante._edad for estudiante in estudiantes)
    return total / len(estudiantes)
def verificar_misma_edad(persona1, persona2):
    return persona1._edad == persona2._edad


estudiante1 = Estudiante("Juan", "Perez", "Gonzales", 20, "123456", "2023001")
estudiante2 = Estudiante("Maria", "Lopez", "Rodriguez", 22, "123457", "2023002")
docente = Docente("Roberto", "Silva", "Mendez", 35, 5000, "PROF-12345")

print("DATOS DE LAS PERSONAS:")
estudiante1.mostrar()
estudiante2.mostrar()
docente.mostrar()
estudiantes = [estudiante1, estudiante2]
promedio_edad = promedio(estudiantes)
print(f"\nPROMEDIO DE EDADES DE ESTUDIANTES: {promedio_edad:.1f} años")

print("\n" + "=" * 40)
print("MODIFICACION DE EDAD")
print("=" * 40)

estudiante1.modificarEdad(21)
estudiante1.mostrar()

print("\n" + "=" * 40)
print("VERIFICACION DE EDADES")
print("=" * 40)

print(f"¿{estudiante1.nombre} tiene la misma edad que {docente.nombre}? {verificar_misma_edad(estudiante1, docente)}")
print(f"¿{estudiante2.nombre} tiene la misma edad que {docente.nombre}? {verificar_misma_edad(estudiante2, docente)}")

print("\n" + "=" * 40)
print("INFORMACION ADICIONAL")
print("=" * 40)

print(f"Total de estudiantes: {len(estudiantes)}")
print(f"Total de docentes: 1")
print(f"Edad del docente: {docente._edad} años")
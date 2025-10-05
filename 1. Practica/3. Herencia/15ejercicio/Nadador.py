from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def sueldo_total(self):
        pass

    def mostrar_datos(self):
        print(f"   Nombre: {self.nombre}")
        print(f"   Sueldo Total: {self.sueldo_total():.2f} Bs.")

class Chef(Empleado):
    def __init__(self, nombre, horaExtra, tipo, sueldoHora):
        super().__init__(nombre)
        self.horaExtra = horaExtra
        self.tipo = tipo
        self.sueldoHora = sueldoHora

    def sueldo_total(self):
        sueldo_base = self.sueldoHora * 160
        pago_extra = self.horaExtra * self.sueldoHora * 1.5
        return sueldo_base + pago_extra

    def mostrar_datos(self):
        print(f"\nCHEF")
        print("-" * 30)
        super().mostrar_datos()
        print(f"   Horas Extra: {self.horaExtra}")
        print(f"   Tipo: {self.tipo}")
        print(f"   Sueldo por Hora: {self.sueldoHora} Bs.")

class Mesero(Empleado):
    def __init__(self, nombre, propina, horaExtra, sueldoHora):
        super().__init__(nombre)
        self.propina = propina
        self.horaExtra = horaExtra
        self.sueldoHora = sueldoHora

    def sueldo_total(self):
        sueldo_base = self.sueldoHora * 160
        pago_extra = self.horaExtra * self.sueldoHora * 1.25
        return sueldo_base + pago_extra + self.propina

    def mostrar_datos(self):
        print(f"\nMESERO")
        print("-" * 30)
        super().mostrar_datos()
        print(f"   Propina: {self.propina} Bs.")
        print(f"   Horas Extra: {self.horaExtra}")
        print(f"   Sueldo por Hora: {self.sueldoHora} Bs.")


class Administrativo(Empleado):
    def __init__(self, nombre, cargo):
        super().__init__(nombre)
        self.cargo = cargo

    def sueldo_total(self):
        sueldos = {
            "Gerente": 8000,
            "Contador": 6000,
            "Secretario": 4000,
            "Recepcionista": 3500
        }
        return sueldos.get(self.cargo, 5000)

    def mostrar_datos(self):
        print(f"\nADMINISTRATIVO")
        print("-" * 30)
        super().mostrar_datos()
        print(f"   Cargo: {self.cargo}")
print("RATATOUILLE\n")

chef = Chef("Antonio ", 20, "Ejecutivo", 50)
mesero1 = Mesero("Carlos ", 1200, 15, 25)
mesero2 = Mesero("Maria ", 1500, 18, 23)
admin1 = Administrativo("aura", "Gerente")
admin2 = Administrativo("Pedro ", "Contador")
empleados = [chef, mesero1, mesero2, admin1, admin2]

print(" LISTA COMPLETA DE EMPLEADOS ")
for empleado in empleados:
    empleado.mostrar_datos()

def empleados_con_sueldo_x(sueldo_objetivo, lista_empleados):
    print(f"\nEMPLEADOS CON SUELDO TOTAL DE {sueldo_objetivo} Bs.:")
    encontrados = False
    for emp in lista_empleados:
        if emp.sueldo_total() == sueldo_objetivo:
            print(f"   {emp.nombre} - {type(emp).__name__}")
            encontrados = True
    if not encontrados:
        print("   No se encontraron empleados con ese sueldo")
print("BUSQUEDA POR SUELDO TOTAL")
empleados_con_sueldo_x(10000, empleados)
empleados_con_sueldo_x(6000, empleados)
empleados_con_sueldo_x(5000, empleados)
total_nomina = sum(emp.sueldo_total() for emp in empleados)
print(f"Total nomina: {total_nomina:.2f} Bs.")
for emp in empleados:
    if isinstance(emp, Chef):
        print(f"Chef {emp.nombre}:")
        print(f"   Base: 160h * {emp.sueldoHora}Bs/h = {160 * emp.sueldoHora} Bs.")
        print(f"   Extra: {emp.horaExtra}h * {emp.sueldoHora}Bs/h * 1.5 = {emp.horaExtra * emp.sueldoHora * 1.5} Bs.")
        print(f"   TOTAL: {emp.sueldo_total()} Bs.")

    elif isinstance(emp, Mesero):
        print(f"Mesero {emp.nombre}:")
        print(f"   Base: 160h * {emp.sueldoHora}Bs/h = {160 * emp.sueldoHora} Bs.")
        print(f"   Extra: {emp.horaExtra}h * {emp.sueldoHora}Bs/h * 1.25 = {emp.horaExtra * emp.sueldoHora * 1.25} Bs.")
        print(f"   Propina: {emp.propina} Bs.")
        print(f"   TOTAL: {emp.sueldo_total()} Bs.")

    elif isinstance(emp, Administrativo):
        print(f"Administrativo {emp.nombre}:")
        print(f"   Sueldo fijo: {emp.sueldo_total()} Bs.")
print(f"Total Chef: 1")
print(f"Total Meseros: 2")
print(f"Total Administrativos: 2")
print(f"Total empleados: {len(empleados)}")
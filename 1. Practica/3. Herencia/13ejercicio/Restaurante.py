from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, sueldoHora, horaExtra=0):
        self.nombre = nombre
        self.sueldoHora = sueldoHora
        self.horaExtra = horaExtra

    @abstractmethod
    def sueldo_total(self):
        pass

    def mostrar_datos(self):
        print(f"   Nombre: {self.nombre}")
        print(f"   Sueldo por Hora: {self.sueldoHora} Bs.")
        print(f"   Horas Extra: {self.horaExtra}")
        print(f"   Sueldo Total: {self.sueldo_total():.2f} Bs.")


class Chef(Empleado):
    def __init__(self, nombre, sueldoHora, horaExtra, tipo):
        super().__init__(nombre, sueldoHora, horaExtra)
        self.tipo = tipo

    def sueldo_total(self):
        sueldo_base = self.sueldoHora * 160
        pago_extra = self.horaExtra * self.sueldoHora * 1.5
        return sueldo_base + pago_extra

    def mostrar_datos(self):
        print(f"\nCHEF")
        print("-" * 30)
        super().mostrar_datos()
        print(f"   Tipo: {self.tipo}")


class Mesero(Empleado):
    def __init__(self, nombre, sueldoHora, horaExtra, propina):
        super().__init__(nombre, sueldoHora, horaExtra)
        self.propina = propina

    def sueldo_total(self):
        sueldo_base = self.sueldoHora * 160
        pago_extra = self.horaExtra * self.sueldoHora * 1.25
        return sueldo_base + pago_extra + self.propina

    def mostrar_datos(self):
        print(f"\nMESERO")
        print("-" * 30)
        super().mostrar_datos()
        print(f"   Propina: {self.propina} Bs.")


class Administrativo(Empleado):
    def __init__(self, nombre, cargo):
        super().__init__(nombre, 0, 0)
        self.cargo = cargo
        self.sueldo_mensual = self._calcular_sueldo_fijo()

    def _calcular_sueldo_fijo(self):
        sueldos = {
            "Gerente": 8000,
            "Contador": 6000,
            "Secretario": 4000,
            "Recepcionista": 3500
        }
        return sueldos.get(self.cargo, 5000)

    def sueldo_total(self):
        return self.sueldo_mensual

    def mostrar_datos(self):
        print(f"\nADMINISTRATIVO")
        print("-" * 30)
        print(f"   Nombre: {self.nombre}")
        print(f"   Cargo: {self.cargo}")
        print(f"   Sueldo Total: {self.sueldo_total():.2f} Bs.")
print("== RESTAURANTE RATATOUILLE ==\n")
print("SISTEMA DE GESTION DE PERSONAL\n")
chef = Chef("Antonio Gomez", 50, 20, "Ejecutivo")
mesero1 = Mesero("Carlos Lopez", 25, 15, 1200)
mesero2 = Mesero("Maria Rodriguez", 23, 18, 1500)
admin1 = Administrativo("Laura Martinez", "Gerente")
admin2 = Administrativo("Pedro Sanchez", "Contador")
empleados = [chef, mesero1, mesero2, admin1, admin2]
print("= LISTA COMPLETA DE EMPLEADOS =")
for empleado in empleados:
    empleado.mostrar_datos()

def empleados_con_sueldo_total(sueldo_objetivo, lista_empleados):
    print(f"\nEMPLEADOS CON SUELDO TOTAL DE {sueldo_objetivo} Bs.:")
    encontrados = [emp for emp in lista_empleados if emp.sueldo_total() == sueldo_objetivo]

    if encontrados:
        for emp in encontrados:
            tipo = type(emp).__name__
            print(f"   {emp.nombre} - {tipo}")
    else:
        print("   No se encontraron empleados con ese sueldo total")

print("BUSQUEDA POR SUELDO TOTAL")


empleados_con_sueldo_total(11000, empleados)  #
empleados_con_sueldo_total(6000, empleados)

def empleados_con_sueldo_aproximado(sueldo_objetivo, lista_empleados, margen=10):
    print(f"\nEMPLEADOS CON SUELDO TOTAL APROXIMADO A {sueldo_objetivo} Bs. (+/- {margen} Bs.):")
    encontrados = [emp for emp in lista_empleados
                   if abs(emp.sueldo_total() - sueldo_objetivo) <= margen]

    if encontrados:
        for emp in encontrados:
            tipo = type(emp).__name__
            print(f"   {emp.nombre} - {tipo} - {emp.sueldo_total():.2f} Bs.")
    else:
        print("   No se encontraron empleados con ese sueldo")
empleados_con_sueldo_aproximado(5500, empleados)
empleados_con_sueldo_aproximado(8000, empleados)
print("RESUMEN FINANCIERO")
total_nomina = sum(emp.sueldo_total() for emp in empleados)
sueldo_promedio = total_nomina / len(empleados)
print(f"Total nomina: {total_nomina:.2f} Bs.")
print(f"Sueldo promedio: {sueldo_promedio:.2f} Bs.")
tipos_empleado = {}
for emp in empleados:
    tipo = type(emp).__name__
    if tipo in tipos_empleado:
        tipos_empleado[tipo] += 1
    else:
        tipos_empleado[tipo] = 1

print(f"\nDistribucion de empleados:")
for tipo, cantidad in tipos_empleado.items():
    print(f"   {tipo}: {cantidad}")

print("DETALLE DE CALCULO DE SUELDOS")
for emp in empleados:
    tipo = type(emp).__name__
    if tipo == "Chef":
        print(f"{emp.nombre} (Chef):")
        print(f"   Base: 160h * {emp.sueldoHora}Bs/h = {160 * emp.sueldoHora} Bs.")
        print(f"   Extra: {emp.horaExtra}h * {emp.sueldoHora}Bs/h * 1.5 = {emp.horaExtra * emp.sueldoHora * 1.5} Bs.")
    elif tipo == "Mesero":
        print(f"{emp.nombre} (Mesero):")
        print(f"   Base: 160h * {emp.sueldoHora}Bs/h = {160 * emp.sueldoHora} Bs.")
        print(f"   Extra: {emp.horaExtra}h * {emp.sueldoHora}Bs/h * 1.25 = {emp.horaExtra * emp.sueldoHora * 1.25} Bs.")
        print(f"   Propina: {emp.propina} Bs.")
    elif tipo == "Administrativo":
        print(f"{emp.nombre} (Administrativo):")
        print(f"   Sueldo fijo por cargo '{emp.cargo}': {emp.sueldo_mensual} Bs.")
class Persona:
    def __init__(self, CI=None, nombre=None, apellido=None):
        self._nombre = nombre
        self._apellido = apellido
        self._CI = CI

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_CI(self):
        return self._CI

    def set_CI(self, CI):
        self._CI = CI


class Cliente(Persona):
    def __init__(self, nombre, apellido, CI, randompza, ticCliente):
        super().__init__(CI, nombre, apellido)
        self.__randompza = randompza
        self.__ticCliente = ticCliente

    def get_randompza(self):
        return self.__randompza

    def set_randompza(self, randompza):
        self.__randompza = randompza

    def get_ticCliente(self):
        return self.__ticCliente

    def set_ticCliente(self, ticCliente):
        self.__ticCliente = ticCliente


class Jefe(Persona):
    def __init__(self, sucursal, tips, CI, nombre=None, apellido=None):
        if nombre and apellido:
            super().__init__(CI, nombre, apellido)
        else:
            super().__init__(CI)
        self.__sucursal = sucursal
        self.__tips = tips

    def get_sucursal(self):
        return self.__sucursal

    def set_sucursal(self, sucursal):
        self.__sucursal = sucursal

    def get_tips(self):
        return self.__tips

    def set_tips(self, tips):
        self.__tips = tips


jefe1 = Jefe("Sucursal Central", "Gestion eficiente", "1234567", "Carlos", "Gomez")
print("Jefe:", jefe1.get_nombre(), jefe1.get_apellido())
print("Sucursal:", jefe1.get_sucursal())
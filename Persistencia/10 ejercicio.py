import os
import json
import base64

class Jugador:
    def __init__(self, nombre, nivel, puntaje):
        self.nombre = nombre
        self.nivel = nivel
        self.puntaje = puntaje

    def to_dict(self):
        return {"nombre": self.nombre, "nivel": self.nivel, "puntaje": self.puntaje}


class ConjuntoDatos:
    def __init__(self, nombre, num_instancias, algoritmo):
        self.nombre = nombre
        self.num_instancias = num_instancias
        self.algoritmo = algoritmo

    def to_dict(self):
        return {"nombre": self.nombre, "num_instancias": self.num_instancias, "algoritmo": self.algoritmo}


class UsuarioSeguro:
    def __init__(self, username, password):
        self.username = username
        self.password = base64.b64encode(password.encode()).decode()

    def to_dict(self):
        return {"username": self.username, "password": self.password}


class Empresa:
    def __init__(self, nombre, rubro, num_empleados):
        self.nombre = nombre
        self.rubro = rubro
        self.num_empleados = num_empleados

    def to_dict(self):
        return {"nombre": self.nombre, "rubro": self.rubro, "num_empleados": self.num_empleados}


class TransaccionNFC:
    def __init__(self, id_transaccion, monto, fecha):
        self.id_transaccion = id_transaccion
        self.monto = monto
        self.fecha = fecha

    def to_dict(self):
        return {"id_transaccion": self.id_transaccion, "monto": self.monto, "fecha": self.fecha}


class DispositivoWiFi:
    def __init__(self, mac, nombre, velocidad):
        self.mac = mac
        self.nombre = nombre
        self.velocidad = velocidad

    def to_dict(self):
        return {"mac": self.mac, "nombre": self.nombre, "velocidad": self.velocidad}


class ArchivoJSON:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def guardar(self, obj):
        datos = obj.to_dict()
        if os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, "r") as f:
                lista = json.load(f)
        else:
            lista = []
        lista.append(datos)
        with open(self.nombre_archivo, "w") as f:
            json.dump(lista, f, indent=4)

    def mostrar_todos(self):
        if not os.path.exists(self.nombre_archivo):
            print("No hay datos")
            return
        with open(self.nombre_archivo, "r") as f:
            lista = json.load(f)
        for d in lista:
            print(d)

    def buscar(self, clave, valor):
        if not os.path.exists(self.nombre_archivo):
            print("No hay datos")
            return
        with open(self.nombre_archivo, "r") as f:
            lista = json.load(f)
        for d in lista:
            if d.get(clave) == valor:
                print("Encontrado:", d)
                return
        print(f"No encontrado: {valor}")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Desarrollo de Software")
        print("2. Inteligencia Artificial")
        print("3. Seguridad de la Información")
        print("4. Ingeniería en Sistemas")
        print("5. Ciencias de la Computación")
        print("6. Redes y TIC")
        print("7. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            menu_generico("jugadores.json", Jugador, ["nombre", "nivel", "puntaje"], "nombre")
        elif opcion == "2":
            menu_generico("dataset.json", ConjuntoDatos, ["nombre", "num_instancias", "algoritmo"], "nombre")
        elif opcion == "3":
            menu_generico("usuarios_seguro.json", UsuarioSeguro, ["username", "password"], "username", descifrar=True)
        elif opcion == "4":
            menu_generico("empresas.json", Empresa, ["nombre", "rubro", "num_empleados"], "nombre")
        elif opcion == "5":
            menu_generico("cobros_nfc.json", TransaccionNFC, ["id_transaccion", "monto", "fecha"], "id_transaccion")
        elif opcion == "6":
            menu_generico("dispositivos_wifi.json", DispositivoWiFi, ["mac", "nombre", "velocidad"], "mac")
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")


def menu_generico(nombre_archivo, clase_obj, campos, campo_busqueda, descifrar=False):
    archivo = ArchivoJSON(nombre_archivo)
    while True:
        print(f"\n--- {nombre_archivo.replace('.json','').capitalize()} ---")
        print("1. Agregar")
        print("2. Mostrar todos")
        print("3. Buscar")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            valores = []
            for c in campos:
                valor = input(f"{c.capitalize()}: ")
                valores.append(valor)
            if clase_obj == UsuarioSeguro:
                obj = clase_obj(valores[0], valores[1])
            else:
                obj = clase_obj(*valores)
            archivo.guardar(obj)
            print("Agregado")

        elif opcion == "2":
            if descifrar:
                if not os.path.exists(nombre_archivo):
                    print("No hay datos")
                    continue
                with open(nombre_archivo, "r") as f:
                    lista = json.load(f)
                for d in lista:
                    d_copy = d.copy()
                    d_copy["password"] = base64.b64decode(d_copy["password"]).decode()
                    print(d_copy)
            else:
                archivo.mostrar_todos()

        elif opcion == "3":
            valor = input(f"Ingrese {campo_busqueda}: ")
            if descifrar:
                if not os.path.exists(nombre_archivo):
                    print("No hay datos")
                    continue
                with open(nombre_archivo, "r") as f:
                    lista = json.load(f)
                for d in lista:
                    if d.get(campo_busqueda) == valor:
                        d_copy = d.copy()
                        d_copy["password"] = base64.b64decode(d_copy["password"]).decode()
                        print("Encontrado:", d_copy)
                        break
                else:
                    print("No encontrado:", valor)
            else:
                archivo.buscar(campo_busqueda, valor)

        elif opcion == "4":
            break
        else:
            print("Opción no válida")


def crear_datos_ejemplo():
    jugadores = [
        Jugador("Player1", "10", "1500"),
        Jugador("Player2", "5", "800"),
        Jugador("Player3", "15", "2200")
    ]
    for j in jugadores:
        ArchivoJSON("jugadores.json").guardar(j)

    datasets = [
        ConjuntoDatos("Iris", "150", "KNN"),
        ConjuntoDatos("MNIST", "70000", "Red Neuronal"),
        ConjuntoDatos("CIFAR-10", "60000", "CNN")
    ]
    for d in datasets:
        ArchivoJSON("dataset.json").guardar(d)

    usuarios = [
        UsuarioSeguro("admin", "admin123"),
        UsuarioSeguro("user1", "password1"),
        UsuarioSeguro("user2", "segura456")
    ]
    for u in usuarios:
        ArchivoJSON("usuarios_seguro.json").guardar(u)

    empresas = [
        Empresa("TechCorp", "Tecnología", "500"),
        Empresa("BuildCo", "Construcción", "250"),
        Empresa("FoodInc", "Alimentación", "100")
    ]
    for e in empresas:
        ArchivoJSON("empresas.json").guardar(e)

    transacciones = [
        TransaccionNFC("T001", "25.50", "15/11/2025"),
        TransaccionNFC("T002", "100.00", "14/11/2025"),
        TransaccionNFC("T003", "50.75", "13/11/2025")
    ]
    for t in transacciones:
        ArchivoJSON("cobros_nfc.json").guardar(t)

    dispositivos = [
        DispositivoWiFi("AA:BB:CC:DD:EE:01", "Laptop-1", "1200"),
        DispositivoWiFi("AA:BB:CC:DD:EE:02", "Smartphone-1", "800"),
        DispositivoWiFi("AA:BB:CC:DD:EE:03", "Tablet-1", "600")
    ]
    for d in dispositivos:
        ArchivoJSON("dispositivos_wifi.json").guardar(d)


crear_datos_ejemplo()
menu_principal()

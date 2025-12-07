import json
import os


class Libro:
    def __init__(self, codigo, titulo, precio):
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.vendidos = 0
        self.prestados = 0

    def vender(self, cantidad=1):
        self.vendidos += cantidad

    def prestar(self):
        self.prestados += 1

    def devolver(self):
        if self.prestados > 0:
            self.prestados -= 1

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "precio": self.precio,
            "vendidos": self.vendidos,
            "prestados": self.prestados
        }


class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id = id_cliente
        self.nombre = nombre
        self.libros_comprados = []  # Lista de códigos de libros comprados
        self.libros_prestados = []  # Lista de códigos de libros prestados

    def comprar_libro(self, codigo_libro):
        if codigo_libro not in self.libros_comprados:
            self.libros_comprados.append(codigo_libro)

    def prestar_libro(self, codigo_libro):
        if codigo_libro not in self.libros_prestados:
            self.libros_prestados.append(codigo_libro)

    def devolver_libro(self, codigo_libro):
        if codigo_libro in self.libros_prestados:
            self.libros_prestados.remove(codigo_libro)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "libros_comprados": self.libros_comprados,
            "libros_prestados": self.libros_prestados
        }


class ArchivoBiblioteca:
    def __init__(self):
        self.libros_file = "libros.json"
        self.clientes_file = "clientes.json"

    def guardar_libro(self, libro):
        libros = self._cargar_libros()

        for i, l in enumerate(libros):
            if l.codigo == libro.codigo:
                libros[i] = libro
                break
        else:
            libros.append(libro)
        self._guardar_libros(libros)

    def guardar_cliente(self, cliente):
        clientes = self._cargar_clientes()
        for i, c in enumerate(clientes):
            if c.id == cliente.id:
                clientes[i] = cliente
                break
        else:
            clientes.append(cliente)
        self._guardar_clientes(clientes)

    def _cargar_libros(self):
        if not os.path.exists(self.libros_file):
            return []
        with open(self.libros_file, 'r') as f:
            data = json.load(f)
        libros = []
        for item in data:
            libro = Libro(item["codigo"], item["titulo"], item["precio"])
            libro.vendidos = item["vendidos"]
            libro.prestados = item["prestados"]
            libros.append(libro)
        return libros

    def _cargar_clientes(self):
        if not os.path.exists(self.clientes_file):
            return []
        with open(self.clientes_file, 'r') as f:
            data = json.load(f)
        clientes = []
        for item in data:
            cliente = Cliente(item["id"], item["nombre"])
            cliente.libros_comprados = item["libros_comprados"]
            cliente.libros_prestados = item["libros_prestados"]
            clientes.append(cliente)
        return clientes

    def _guardar_libros(self, libros):
        with open(self.libros_file, 'w') as f:
            json.dump([l.to_dict() for l in libros], f, indent=2)

    def _guardar_clientes(self, clientes):
        with open(self.clientes_file, 'w') as f:
            json.dump([c.to_dict() for c in clientes], f, indent=2)

    def listar_libros_por_precio(self, min_precio, max_precio):
        libros = self._cargar_libros()
        resultado = [l for l in libros if min_precio <= l.precio <= max_precio]
        return resultado

    def ingreso_total_libro(self, codigo):
        libros = self._cargar_libros()
        for libro in libros:
            if libro.codigo == codigo:
                return libro.precio * libro.vendidos
        return 0

    def libros_nunca_vendidos(self):
        libros = self._cargar_libros()
        resultado = [l for l in libros if l.vendidos == 0]
        return resultado

    def clientes_que_compraron(self, codigo_libro):
        clientes = self._cargar_clientes()
        resultado = [c for c in clientes if codigo_libro in c.libros_comprados]
        return resultado

    def libro_mas_prestado(self):
        libros = self._cargar_libros()
        if not libros:
            return None
        return max(libros, key=lambda x: x.prestados)

    def cliente_mas_prestamos(self):
        clientes = self._cargar_clientes()
        if not clientes:
            return None
        return max(clientes, key=lambda x: len(x.libros_prestados))

    def mostrar_libros(self):
        libros = self._cargar_libros()
        if not libros:
            print("No hay libros registrados.")
            return
        print("\n=== LISTA DE LIBROS ===")
        for libro in libros:
            print(f"Código: {libro.codigo}")
            print(f"Título: {libro.titulo}")
            print(f"Precio: ${libro.precio:.2f}")
            print(f"Vendidos: {libro.vendidos}")
            print(f"Prestados: {libro.prestados}")
            print("-" * 30)

    def mostrar_clientes(self):
        clientes = self._cargar_clientes()
        if not clientes:
            print("No hay clientes registrados.")
            return
        print("\n=== LISTA DE CLIENTES ===")
        for cliente in clientes:
            print(f"ID: {cliente.id}")
            print(f"Nombre: {cliente.nombre}")
            print(f"Libros comprados: {', '.join(cliente.libros_comprados) if cliente.libros_comprados else 'Ninguno'}")
            print(f"Libros prestados: {', '.join(cliente.libros_prestados) if cliente.libros_prestados else 'Ninguno'}")
            print("-" * 30)


archivo = ArchivoBiblioteca()

libro1 = Libro("L001", "El Principito", 10.99)
libro2 = Libro("L002", "Cien Años de Soledad", 15.50)
libro3 = Libro("L003", "Don Quijote", 12.00)


libro1.vender(5)
libro2.vender(3)
libro3.vender(0)

libro1.prestar()
libro1.prestar()
libro2.prestar()


archivo.guardar_libro(libro1)
archivo.guardar_libro(libro2)
archivo.guardar_libro(libro3)

cliente1 = Cliente(1, "Juan Pérez")
cliente1.comprar_libro("L001")
cliente1.prestar_libro("L001")
cliente1.prestar_libro("L002")

cliente2 = Cliente(2, "María Gómez")
cliente2.comprar_libro("L001")
cliente2.comprar_libro("L002")
cliente2.prestar_libro("L001")

cliente3 = Cliente(3, "Carlos López")
cliente3.comprar_libro("L002")

archivo.guardar_cliente(cliente1)
archivo.guardar_cliente(cliente2)
archivo.guardar_cliente(cliente3)

archivo.mostrar_libros()
archivo.mostrar_clientes()

print("\n a) Libros entre BS 10 y  BS 15 ")
libros_rango = archivo.listar_libros_por_precio(10, 15)
for libro in libros_rango:
    print(f"- {libro.titulo}: BS {libro.precio:.2f}")

print("\nb) Ingreso total por libro 'El Principito' ")
ingreso = archivo.ingreso_total_libro("L001")
print(f"Ingreso total: BS {ingreso:.2f}")

print("\n c) Libros nunca vendidos ")
no_vendidos = archivo.libros_nunca_vendidos()
if no_vendidos:
    for libro in no_vendidos:
        print(f"- {libro.titulo}")
else:
    print("No hay libros sin vender.")

print("\n d) Clientes que compraron 'El Principito' ")
compradores = archivo.clientes_que_compraron("L001")
for cliente in compradores:
    print(f"- {cliente.nombre}")

print("\n e) Libro más prestado ")
mas_prestado = archivo.libro_mas_prestado()
if mas_prestado:
    print(f"Libro: {mas_prestado.titulo}, Prestado {mas_prestado.prestados} veces")

print("\n f) Cliente con más préstamos ")
cliente_prestamos = archivo.cliente_mas_prestamos()
if cliente_prestamos:
    print(f"Cliente: {cliente_prestamos.nombre}, Préstamos: {len(cliente_prestamos.libros_prestados)}")



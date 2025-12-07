import json
import os


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio
        }


class ArchivoProducto:
    def __init__(self, nombre_archivo="productos.json"):
        self.nombre_archivo = nombre_archivo

    def crear_archivo(self):
        if not os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, 'w') as f:
                json.dump([], f)

    def guardar_producto(self, producto):
        productos = self.cargar_productos()
        productos.append(producto)
        with open(self.nombre_archivo, 'w') as f:
            json.dump([p.to_dict() for p in productos], f, indent=2)

    def cargar_productos(self):
        if not os.path.exists(self.nombre_archivo):
            return []
        with open(self.nombre_archivo, 'r') as f:
            data = json.load(f)
        return [Producto(p["codigo"], p["nombre"], p["precio"]) for p in data]

    def buscar_producto(self, codigo):
        productos = self.cargar_productos()
        for producto in productos:
            if producto.codigo == codigo:
                return producto
        return None

    def promedio_precios(self):
        productos = self.cargar_productos()
        if not productos:
            return 0
        total = sum(p.precio for p in productos)
        return total / len(productos)

    def producto_mas_caro(self):
        productos = self.cargar_productos()
        if not productos:
            return None
        return max(productos, key=lambda x: x.precio)



archivo = ArchivoProducto("productos.json")
archivo.crear_archivo()

p1 = Producto(1, "Laptop", 1500.0)
p2 = Producto(2, "Mouse", 25.0)

archivo.guardar_producto(p1)
archivo.guardar_producto(p2)

print(f"Promedio precios: Bs {archivo.promedio_precios():.2f}")
mas_caro = archivo.producto_mas_caro()
print(f"Producto más caro: {mas_caro.nombre} - Bs {mas_caro.precio}")
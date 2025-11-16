+
public class ProductoNoEncontradoException extends Exception {
    public ProductoNoEncontradoException(String msg) {
        super(msg);
    }
}

class StockInsuficienteException extends Exception {
    public StockInsuficienteException(String msg) {
        super(msg);
    }
}

class Producto {
    private String codigo;
    private String nombre;
    private double precio;
    private int stock;

    public Producto(String codigo, String nombre, double precio, int stock) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    public String getCodigo() { return codigo; }
    public String getNombre() { return nombre; }
    public double getPrecio() { return precio; }
    public int getStock() { return stock; }
    public void setStock(int stock) { this.stock = stock; }
}
 class Inventario {
    private Producto[] productos;
    private int numProductos;

    public Inventario(int maxProductos) {
        this.productos = new Producto[maxProductos];
        this.numProductos = 0;
    }

    public void agregarProducto(Producto p) throws Exception {
        if (p.getPrecio() < 0 || p.getStock() < 0) {
            throw new IllegalArgumentException("Precio o stock negativo");
        }
        for (int i = 0; i < numProductos; i++) {
            if (productos[i].getCodigo().equals(p.getCodigo())) {
                throw new Exception("Código ya existe");
            }
        }
        if (numProductos < productos.length) {
            productos[numProductos++] = p;
        }
    }

    public Producto buscarProducto(String codigo) throws ProductoNoEncontradoException {
        for (int i = 0; i < numProductos; i++) {
            if (productos[i].getCodigo().equals(codigo)) {
                return productos[i];
            }
        }
        throw new ProductoNoEncontradoException("Producto no encontrado");
    }

    public void venderProducto(String codigo, int cantidad) throws Exception {
        Producto p = buscarProducto(codigo);
        if (p.getStock() < cantidad) {
            throw new StockInsuficienteException("Stock insuficiente");
        }
        p.setStock(p.getStock() - cantidad);
    }
}

class Prueba {
    public static void main(String[] args) {
        Inventario inv = new Inventario(10);
        try {
            inv.agregarProducto(new Producto("P1", "Prod1", 10.0, 5));
            inv.agregarProducto(new Producto("P2", "Prod2", -5.0, 3)); // Error
        } catch (Exception e) {
            System.out.println("Error agregar: " + e.getMessage());
        }

        try {
            Producto p = inv.buscarProducto("P1");
            System.out.println("Encontrado: " + p.getNombre());
            inv.venderProducto("P1", 3);
            System.out.println("Stock después venta: " + p.getStock());
            inv.venderProducto("P1", 3); // Error stock
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
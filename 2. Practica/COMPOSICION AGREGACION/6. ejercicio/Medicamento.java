
public class Medicamento {
    private String nombre;
    private double precio;
    private Registro[] registros;
    private int numRegistros;
    private static final int MAX_REGISTROS = 100;

    public Medicamento(String nombre, double precio, int maxRegistros) {
        this.nombre = nombre;
        this.precio = precio;
        this.registros = new Registro[maxRegistros < MAX_REGISTROS ? maxRegistros : MAX_REGISTROS];
        this.numRegistros = 0;
    }

    public void agregarRegistro(Registro r) {
        if (numRegistros < registros.length) {
            registros[numRegistros++] = r;
        }
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    @Override
    public String toString() {
        return "Medicamento{nombre='" + nombre + "', precio=" + precio + "}";
    }
}

public class Registro {
    private String fecha;
    private int cantidad;

    public Registro(String fecha, int cantidad) {
        this.fecha = fecha;
        this.cantidad = cantidad;
    }

    // Getters
    public String getFecha() { return fecha; }
    public int getCantidad() { return cantidad; }
}
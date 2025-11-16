
public class Bailarin {
    private String nombre;
    private int edad;
    private Fraternidad fraternidad;
    private Facultad facultad;

    public Bailarin(String nombre, int edad, Facultad facultad) {
        this.nombre = nombre;
        this.edad = edad;
        this.facultad = facultad;
    }

    public void setFraternidad(Fraternidad fraternidad) {
        this.fraternidad = fraternidad;
    }

    public String getNombre() { return nombre; }
    public int getEdad() { return edad; }
    public Facultad getFacultad() { return facultad; }
    public Fraternidad getFraternidad() { return fraternidad; }
}
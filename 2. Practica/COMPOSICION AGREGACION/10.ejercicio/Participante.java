
public class Participante {
    private String nombre;
    private String apellido;
    private int edad;
    private String ci;

    public Participante(String nombre, String apellido, int edad, String ci) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.ci = ci;
    }

    public String getNombre() { return nombre; }
    public String getApellido() { return apellido; }
    public int getEdad() { return edad; }
    public String getCi() { return ci; }
}
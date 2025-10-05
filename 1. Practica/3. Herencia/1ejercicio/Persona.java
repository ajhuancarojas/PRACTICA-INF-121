package Herencia;

public class Persona {
    protected String nombre;
    protected String apellido;
    protected String CI;
    public Persona() {
    }

    public Persona(String CI) {
        this.CI = CI;
    }
    public Persona(String nombre, String apellido, String CI) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.CI = CI;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getCI() {
        return CI;
    }

    public void setCI(String CI) {
        this.CI = CI;
    }
}
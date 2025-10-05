
package M;
public class Persona {
    public String nombre;
    public int edad;

    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    void mostrar() {
        System.out.println("Nombre: " + nombre + " | Edad: " + edad);
    }
}

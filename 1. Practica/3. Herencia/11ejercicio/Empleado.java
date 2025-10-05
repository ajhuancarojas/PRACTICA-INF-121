
package M;
public class Empleado extends Persona {
    public double sueldo;
    public String cargo;

    Empleado(String nombre, int edad, double sueldo, String cargo) {
        super(nombre, edad);
        this.sueldo = sueldo;
        this.cargo = cargo;
    }

    void mostrar() {
        super.mostrar();
        System.out.println("Cargo: " + cargo + " | Sueldo: " + sueldo);
    }
}



package M;
public class Policia extends Empleado {
    String rango;
    String distrito;

    Policia(String nombre, int edad, double sueldo, String cargo, String rango, String distrito) {
        super(nombre, edad, sueldo, cargo);
        this.rango = rango;
        this.distrito = distrito;
    }

    void mostrar() {
        super.mostrar();
        System.out.println("Rango: " + rango + " | Distrito: " + distrito);
    }
}


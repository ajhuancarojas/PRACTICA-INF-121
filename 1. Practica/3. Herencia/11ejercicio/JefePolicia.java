
package M;
public class JefePolicia extends Policia implements OperacionesJefe {
    String grado;
    int añosServicio;

    JefePolicia(String nombre, int edad, double sueldo, String cargo, String rango, String distrito, String grado, int añosServicio) {
        super(nombre, edad, sueldo, cargo, rango, distrito);
        this.grado = grado;
        this.añosServicio = añosServicio;
    }

    void mostrar() {
        super.mostrar();
        System.out.println("Grado: " + grado + " | Años: " + añosServicio);
    }

    public void compararSueldo(JefePolicia a, JefePolicia b) {
        if (a.sueldo > b.sueldo)
            System.out.println(a.nombre + " gana más.");
        else if (a.sueldo < b.sueldo)
            System.out.println(b.nombre + " gana más.");
        else
            System.out.println("Ambos ganan igual.");
    }

    public void compararGrado(JefePolicia a, JefePolicia b) {
        if (a.grado.equalsIgnoreCase(b.grado))
            System.out.println("Mismo grado.");
        else
            System.out.println("Grados distintos.");
    }
}

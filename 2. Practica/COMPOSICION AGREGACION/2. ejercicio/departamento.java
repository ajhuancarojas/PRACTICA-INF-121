
public class departamento {
    private String nombre;
    private String area;
    private Empleado[] empleados;
    private int numEmpleados;

    public departamento(String nombre, String area, int maxEmpleados) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = new Empleado[maxEmpleados];
        this.numEmpleados = 0;
    }

    public void agregarEmpleado(Empleado e) {
        if (numEmpleados < empleados.length) {
            empleados[numEmpleados++] = e;
        }
    }

    public void mostrarEmpleados() {
        System.out.println("Departamento: " + nombre + ", Área: " + area);
        for (int i = 0; i < numEmpleados; i++) {
            System.out.println(" - " + empleados[i].getNombre() + ": Sueldo " + empleados[i].getSueldo());
        }
        System.out.println();
    }

    public void cambioSalario(double nuevoSueldo) {
        for (int i = 0; i < numEmpleados; i++) {
            empleados[i].setSueldo(nuevoSueldo);
        }
    }

    public boolean contieneEmpleado(Empleado e) {
        for (int i = 0; i < numEmpleados; i++) {
            if (empleados[i] == e) {
                return true;
            }
        }
        return false;
    }

    public void moverEmpleadosA(departamento otro) {
        for (int i = 0; i < numEmpleados; i++) {
            otro.agregarEmpleado(empleados[i]);
        }
        numEmpleados = 0;
    }
    public Empleado[] getEmpleados() {
        return empleados;
    }

    public int getNumEmpleados() {
        return numEmpleados;
    }
}

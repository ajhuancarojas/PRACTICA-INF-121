
public class Empresa {
    private String nombre;
    private Empleado[] empleados;
    private int numEmpleados;

    public Empresa(String nombre, int maxEmpleados) {
        this.nombre = nombre;
        this.empleados = new Empleado[maxEmpleados];
        this.numEmpleados = 0;
    }

    public void agregarEmpleado(Empleado e) {
        if (numEmpleados < empleados.length) {
            empleados[numEmpleados++] = e;
        }
    }
    public void mostrarInfo() {
        System.out.println("Empresa: " + nombre);
        for (int i = 0; i < numEmpleados; i++) {
            System.out.println( empleados[i].getNombre() + ", Puesto: " + empleados[i].getPuesto() + ", Salario: " + empleados[i].getSalario());
        }
        System.out.println();
    }

    public String buscarEmpleado(String nombre) {
        for (int i = 0; i < numEmpleados; i++) {
            if (empleados[i].getNombre().equals(nombre)) {
                return empleados[i].getNombre() + ", Puesto: " + empleados[i].getPuesto() + ", Salario: " + empleados[i].getSalario();
            }
        }
        return "No encontrado";
    }

    public void eliminarEmpleado(String nombre) {
        for (int i = 0; i < numEmpleados; i++) {
            if (empleados[i].getNombre().equals(nombre)) {
                for (int j = i; j < numEmpleados - 1; j++) {
                    empleados[j] = empleados[j + 1];
                }
                numEmpleados--;
                return;
            }
        }
    }

    public double promedioSalarial() {
        double total = 0;
        for (int i = 0; i < numEmpleados; i++) {
            total += empleados[i].getSalario();
        }
        return numEmpleados > 0 ? total / numEmpleados : 0;
    }

    public void listarEmpleadosMayorSalario(double valor) {
        System.out.println("Empleados con salario > " + valor + ":");
        for (int i = 0; i < numEmpleados; i++) {
            if (empleados[i].getSalario() > valor) {
                System.out.println(" - " + empleados[i].getNombre());
            }
        }
        System.out.println();
    }
}
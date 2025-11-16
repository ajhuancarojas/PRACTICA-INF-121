
public class pruebaEmpleado {
    public static void main(String[] args) {
        Empresa empresa = new Empresa("TechCorp", 10);
     
        empresa.agregarEmpleado(new Empleado("OOO", "Dev", 2000));
        empresa.agregarEmpleado(new Empleado("PPP", "Manager", 3000));
        empresa.agregarEmpleado(new Empleado("JJJ", "Tester", 1500));
        empresa.mostrarInfo();
        System.out.println("Buscar OO: " + empresa.buscarEmpleado("JJ"));
        empresa.eliminarEmpleado("PP");
        empresa.mostrarInfo();
        System.out.println("Promedio salarial: " + empresa.promedioSalarial());
        empresa.listarEmpleadosMayorSalario(2000);
    }
}


public class pruebaempreado {
    public static void main(String[] args) {
        
        departamento dept1 = new departamento("Ventas", "Comercial", 10);
        for (int i = 1; i <= 5; i++) {
            dept1.agregarEmpleado(new Empleado("Empleado" + i, 1000 + i * 100));
        }
        departamento dept2 = new departamento("IT", "Tecnología", 10); // Sin empleados

        dept1.mostrarEmpleados();
        dept2.mostrarEmpleados();

        dept1.cambioSalario(2000);
        dept1.mostrarEmpleados();
         boolean pertenece = false;
        for (int i = 0; i < dept1.getNumEmpleados(); i++) {
            if (dept2.contieneEmpleado(dept1.getEmpleados()[i])) {
                pertenece = true;
                break;
            }
        }
        System.out.println("Algún empleado de dept1 en dept2? " + pertenece);
        dept1.moverEmpleadosA(dept2);
        dept1.mostrarEmpleados();
        dept2.mostrarEmpleados();
    }
}


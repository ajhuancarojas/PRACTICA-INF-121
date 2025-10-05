package Herencia;
public class pruebaPersona {
     public static void main(String[] args) {
        // Crear un objeto Jefe
        Jefe jefe1 = new Jefe("Sucursal Central", "Gestión eficiente", "1234567", "Carlos", "Gómez");
        
        System.out.println("Jefe: " + jefe1.getNombre() + " " + jefe1.getApellido());
        System.out.println("Sucursal: " + jefe1.getSucursal());
    }
}

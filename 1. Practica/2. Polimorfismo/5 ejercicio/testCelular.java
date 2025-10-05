package polimorfismo;
public class testCelular {
  public static void main(String[] args) {
        Celular c = new Celular("123456789", "ANA CASTRO", 64.0, 9, 8);
        System.out.println("DATOS ANTES DE LOS OPERADORES:");
        c.mostrarDatos();
        System.out.println("\nAPLICANDO OPERADOR ++:");
        c.aumentar();
        c.mostrarDatos();
        System.out.println("\nAPLICANDO OPERADOR -- :");
        c.disminuir();
        c.mostrarDatos();
        System.out.println("\nRESULTADO :");
        c.mostrarDatos();
    }  
}

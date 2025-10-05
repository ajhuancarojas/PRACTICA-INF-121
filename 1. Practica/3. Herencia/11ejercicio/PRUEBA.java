/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package M;

/**
 *
 * @author Alejandra
 */
public class PRUEBA {
    public static void main(String[] args) {
        JefePolicia j1 = new JefePolicia("Carlos", 45, 8000, "Comandante", "Mayor", "Sur", "A", 20);
        JefePolicia j2 = new JefePolicia("Luis", 40, 7500, "Comandante", "Mayor", "Norte", "B", 18);

        System.out.println("=== JEFE 1 ===");
        j1.mostrar();

        System.out.println("\n=== JEFE 2 ===");
        j2.mostrar();

        System.out.println("\n=== COMPARACIONES ===");
        j1.compararSueldo(j1, j2);
        j1.compararGrado(j1, j2);
    }
}

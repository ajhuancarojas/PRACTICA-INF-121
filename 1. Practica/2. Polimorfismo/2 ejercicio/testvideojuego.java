
package polimorfismo;
import java.util.Scanner;

public class testvideojuego {
  public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        Videojuego v1 = new Videojuego();
        Videojuego v2 = new Videojuego("clash royale");
        System.out.println("=== VIDEOJUEGO 1 ===");
        v1.agregarJugadores();
        v1.agregarJugadores(2);
        v1.mostrarDatos();

        System.out.println("\n=== VIDEOJUEGO 2 ===");
        v2.agregarJugadores(4);
        v2.mostrarDatos();

    }
   
}
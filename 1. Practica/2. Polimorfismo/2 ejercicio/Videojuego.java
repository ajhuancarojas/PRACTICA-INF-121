package polimorfismo;
import java.util.Scanner;
public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;
    public Videojuego() {
        this.nombre = "desconocido";
        this.plataforma = "desconocida";
        this.cantidadJugadores = 0;
    }
    public Videojuego(String nombre) {
        this.nombre = nombre;
        this.plataforma = "multiplataforma";
        this.cantidadJugadores = 0;
    }
    public Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = 0;
    }
    public void agregarJugadores() {
        cantidadJugadores++;
        System.out.println("nuevo jugador total: " + cantidadJugadores);
    }
    public void agregarJugadores(int cantidad) {
        if (cantidad > 0) {
            cantidadJugadores += cantidad;
            System.out.println("se agrego " + cantidad + "  total: " + cantidadJugadores);
        } else {
            System.out.println("error...");
        }
    }
    public void agregarJugadores(Scanner scanner) {
        System.out.print("cantidad de jugadores a agregar: ");
        int cantidad = scanner.nextInt();
        agregarJugadores(cantidad);
    }
    public void mostrarDatos() {
        System.out.println("nombre: " + nombre);
        System.out.println("plataforma: " + plataforma);
        System.out.println("cantidad de jugadores: " + cantidadJugadores);
    }
}
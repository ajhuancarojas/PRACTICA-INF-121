
package Herencia;
public class Leon extends Animal {
    public Leon(String nombre, int edad) {
        super(nombre, edad);
    }

    @Override
    public void desplazarse() {
        System.out.println("🦁 " + nombre + " el león camina majestuosamente por la sabana.");
    }
}

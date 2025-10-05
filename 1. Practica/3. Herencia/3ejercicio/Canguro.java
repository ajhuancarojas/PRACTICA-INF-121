package Herencia;
public class Canguro extends Animal {
    public Canguro(String nombre, int edad) {
        super(nombre, edad);
    }

    @Override
    public void desplazarse() {
        System.out.println("🦘 " + nombre + " el canguro salta poderosamente con sus patas traseras.");
    }
}

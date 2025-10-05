package Herencia;
public class Pinguino extends Animal {
    public Pinguino(String nombre, int edad) {
        super(nombre, edad);
    }

    @Override
    public void desplazarse() {
        System.out.println("🐧 " + nombre + " el pingüino se desliza elegantemente sobre el hielo.");
    }
}

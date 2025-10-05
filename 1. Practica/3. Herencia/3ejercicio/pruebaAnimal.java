package Herencia;

public class pruebaAnimal {
    public static void main(String[] args) {
        Animal[] animales = {
            new Leon("Simba", 5),
            new Pinguino("Pingu", 3),
            new Canguro("Jack", 4),
            new Leon("Mufasa", 12)
        };

        for (Animal a : animales) {
            System.out.println("\n---");
            a.mostrarInfo();
            a.desplazarse();
        }
    }
}

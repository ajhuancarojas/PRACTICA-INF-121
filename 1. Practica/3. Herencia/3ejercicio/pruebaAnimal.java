package Herencia;

public class pruebaAnimal {
     public static void main(String[] args) {        
        Animal[] A = new Animal[4];
        A[0] = new Leon("Simba", 2);
        A[1] = new Pinguino("Pingu", 10);
        A[2] = new Canguro("Jack", 9);
        A[3] = new Leon("Carlo", 4);
        
        for (Animal animal : A) {
            System.out.println("\n---");
            animal.mostrarInfo();
            animal.desplazarse();
        }
        System.out.println("Total de animales: " + A.length);
        System.out.println("Tipos de animales:");
        System.out.println(" - Leones: " + contarAnimales(A, "Leon"));
        System.out.println(" - Pingüinos: " + contarAnimales(A, "Pinguino"));
        System.out.println(" - Canguros: " + contarAnimales(A, "Canguro"));
    }

    public static int contarAnimales(Animal[] animales, String tipo) {
        int c = 0;
        for (Animal animal : animales) {
            if (animal.getClass().getSimpleName().equals(tipo)) {
                c++;
            }
        }
        return c;
    }
}

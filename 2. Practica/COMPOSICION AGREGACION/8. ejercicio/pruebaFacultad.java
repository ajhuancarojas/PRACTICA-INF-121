

public class pruebaFacultad {
    public static void main(String[] args) {
    
        Facultad fac1 = new Facultad("Informatica", "Monoblock");
        Facultad fac2 = new Facultad("Derecho", "Central");

        Fraternidad frat1 = new Fraternidad("Frat1", 10);
        Fraternidad frat2 = new Fraternidad("Frat2", 10);

        Bailarin b1 = new Bailarin("Juan", 20, fac1);
        Bailarin b2 = new Bailarin("Maria", 22, fac1);
        Bailarin b3 = new Bailarin("Pedro", 19, fac2);
        Bailarin b4 = new Bailarin("Ana", 21, fac2);
        Bailarin b5 = new Bailarin("Luis", 23, fac1);

        frat1.setEncargado(b1);
        frat1.agregarBailarin(b1);
        frat1.agregarBailarin(b2);
        frat2.setEncargado(b3);
        frat2.agregarBailarin(b3);
        frat2.agregarBailarin(b4);
        frat2.agregarBailarin(b5);

        frat1.agregarBailarin(b3); 
        frat1.mostrar();
        frat2.mostrar();

    }
}

public class Fraternidad {
    private String nombre;
    private Bailarin encargado;
    private Bailarin[] bailarines;
    private int numBailarines;

    public Fraternidad(String nombre, int maxBailarines) {
        this.nombre = nombre;
        this.bailarines = new Bailarin[maxBailarines];
        this.numBailarines = 0;
    }

    public void setEncargado(Bailarin encargado) {
        this.encargado = encargado;
    }

    public void agregarBailarin(Bailarin b) {
        if (numBailarines < bailarines.length && !contieneBailarin(b)) {
            bailarines[numBailarines++] = b;
        } else {
            System.out.println("No se puede agregar: limite o ya existe en otra fraternidad.");
        }
    }

    private boolean contieneBailarin(Bailarin b) {
        for (int i = 0; i < numBailarines; i++) {
            if (bailarines[i] == b) return true;
        }
        return false;
    }

    public void mostrar() {
        System.out.println("Fraternidad: " + nombre + ", Encargado: " + (encargado != null ? encargado.getNombre() : "Ninguno"));
        for (int i = 0; i < numBailarines; i++) {
            System.out.println(" - Bailarin: " + bailarines[i].getNombre() + ", Edad: " + bailarines[i].getEdad() + ", Facultad: " + bailarines[i].getFacultad().getNombre());
        }
    }
}
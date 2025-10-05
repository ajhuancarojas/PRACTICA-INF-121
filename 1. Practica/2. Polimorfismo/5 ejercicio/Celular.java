package polimorfismo;
public class Celular {
    private String nroTel;
    private String dueño;
    private double espacio;
    private int ram;
    private int nroApp;
    public Celular() {
        this.nroTel = "";
        this.dueño = "";
        this.espacio = 0;
        this.ram = 0;
        this.nroApp = 0;
    }
    public Celular(String nroTel, String dueño, double espacio, int ram, int nroApp) {
        this.nroTel = nroTel;
        this.dueño = dueño;
        this.espacio = espacio;
        this.ram = ram;
        this.nroApp = nroApp;
    }
    public void incrementar() {
        this.nroApp += 10;
        System.out.println("Se incremento");
    }
    public void decrementar() {
        if (this.espacio >= 5) {
            this.espacio -= 5;
            System.out.println("disminuyo el espacio");
        } else {
            System.out.println("No hay suficiente espacio ");
        }
    }
    public void mostrarDatos() {
        System.out.println("Numero cell: " + nroTel);
        System.out.println("Dueño: " + dueño);
        System.out.println("Espacio (GB): " + espacio);
        System.out.println("RAM (GB): " + ram);
        System.out.println("N°de Apps: " + nroApp);
        System.out.println();
    }
}

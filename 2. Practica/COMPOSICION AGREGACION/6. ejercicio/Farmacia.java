
public class Farmacia {
    private String nombre;
    private String direccion;
    private Medicamento[] medicamentos;
    private int numMedicamentos;

    public Farmacia(String nombre, String direccion, int maxMedicamentos) {
        this.nombre = nombre;
        this.direccion = direccion;
        this.medicamentos = new Medicamento[maxMedicamentos];
        this.numMedicamentos = 0;
    }

    public Farmacia(String nombre, String direccion) {
        this(nombre, direccion, 50);
    }

    public void agregarMedicamento(Medicamento m) {
        if (numMedicamentos < medicamentos.length) {
            medicamentos[numMedicamentos++] = m;
        } else {
            System.out.println("Farmacia llena. No se puede agregar más medicamentos.");
        }
    }

    public void mostrar() {
        System.out.println("Farmacia: " + nombre + ", Dirección: " + direccion);
        for (int i = 0; i < numMedicamentos; i++) {
            System.out.println(" - " + medicamentos[i]);
        }
        System.out.println();
    }
}
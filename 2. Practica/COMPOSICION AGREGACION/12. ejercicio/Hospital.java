
public class Hospital {
    private final String nombre;
    private Doctor[] doctores;
    private int numDoctores;

    public Hospital(String nombre, int maxDoctores) {
        this.nombre = nombre;
        this.doctores = new Doctor[maxDoctores];
        this.numDoctores = 0;
    }

    public void asignarDoctor(Doctor d) {
        if (numDoctores < doctores.length) {
            doctores[numDoctores++] = d;
        }
    }

    public void mostrarDoctores() {
        System.out.println("Hospital: " + nombre);
        for (int i = 0; i < numDoctores; i++) {
            System.out.println(" - Doctor: " + doctores[i].getNombre() + ", Especialidad: " + doctores[i].getEspecialidad());
        }
        System.out.println();
    }
}

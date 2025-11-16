
public class Evento {
    private String nombre;
    private int inc;
    private Charla[] charlas;
    private int numCharlas;

    public Evento(String nombre, int inc, int maxCharlas) {
        this.nombre = nombre;
        this.inc = inc;
        this.charlas = new Charla[maxCharlas];
        this.numCharlas = 0;
    }

    public void agregarCharla(Charla c) {
        if (numCharlas < charlas.length) {
            charlas[numCharlas++] = c;
        }
    }

    public double edadPromedio() {
        int totalEdad = 0;
        int totalPersonas = 0;
        for (int i = 0; i < numCharlas; i++) {
            Participante[] parts = charlas[i].getParticipantes();
            for (int j = 0; j < charlas[i].getNumParticipantes(); j++) {
                totalEdad += parts[j].getEdad();
                totalPersonas++;
            }
        }
        return totalPersonas > 0 ? (double) totalEdad / totalPersonas : 0;
    }

    public boolean verificarPersona(String nombre, String apellido) {
        for (int i = 0; i < numCharlas; i++) {
            if (charlas[i].tieneParticipanteOSpeaker(nombre, apellido)) {
                return true;
            }
        }
        return false;
    }

    public void eliminarCharlasSpeaker(String ci) {
        for (int i = 0; i < numCharlas; i++) {
            if (charlas[i].getSpeaker().getCi().equals(ci)) {
                for (int j = i; j < numCharlas - 1; j++) {
                    charlas[j] = charlas[j + 1];
                }
                numCharlas--;
                i--;
            }
        }
    }

    public void ordenarCharlasPorParticipantes() {
        for (int i = 0; i < numCharlas - 1; i++) {
            for (int j = 0; j < numCharlas - i - 1; j++) {
                if (charlas[j].getNumParticipantes() < charlas[j + 1].getNumParticipantes()) {
                    Charla temp = charlas[j];
                    charlas[j] = charlas[j + 1];
                    charlas[j + 1] = temp;
                }
            }
        }
    }

    public void mostrarCharlas() {
        for (int i = 0; i < numCharlas; i++) {
            System.out.println("Charla: " + charlas[i].getNumParticipantes() + " participantes");
        }
    }
}
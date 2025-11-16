
public class Charla {
    private String lugar;
    private String nombreCharla;
    private int nroTicket;
    private Participante[] participantes;
    private int numParticipantes;
    private Speaker speaker;

    public Charla(String lugar, String nombreCharla, int nroTicket, Speaker speaker, int maxParticipantes) {
        this.lugar = lugar;
        this.nombreCharla = nombreCharla;
        this.nroTicket = nroTicket;
        this.speaker = speaker;
        this.participantes = new Participante[maxParticipantes];
        this.numParticipantes = 0;
    }

    public void agregarParticipante(Participante p) {
        if (numParticipantes < participantes.length) {
            participantes[numParticipantes++] = p;
        }
    }

    public boolean tieneParticipanteOSpeaker(String nombre, String apellido) {
        for (int i = 0; i < numParticipantes; i++) {
            Participante p = participantes[i];
            if (p.getNombre().equals(nombre) && p.getApellido().equals(apellido)) {
                return true;
            }
        }
        return false;
    }

    public int getNumParticipantes() { return numParticipantes; }
    public Speaker getSpeaker() { return speaker; }
    public Participante[] getParticipantes() { return participantes; }
}
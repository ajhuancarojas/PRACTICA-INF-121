
public class pruebaParticipantes {
    public static void main(String[] args) {
        Evento evento = new Evento("Conferencia", 1, 10);
        Speaker s1 = new Speaker("AI", "123");
        Speaker s2 = new Speaker("Security", "456");

        Charla c1 = new Charla("Sala1", "Talk1", 1, s1, 10);
        c1.agregarParticipante(new Participante("X", "Y", 25, "789"));
        c1.agregarParticipante(new Participante("A", "B", 30, "101"));

        Charla c2 = new Charla("Sala2", "Talk2", 2, s2, 10);
        c2.agregarParticipante(new Participante("C", "D", 28, "112"));

        evento.agregarCharla(c1);
        evento.agregarCharla(c2);

        System.out.println("Edad promedio: " + evento.edadPromedio());
        System.out.println("Persona X Y presente? " + evento.verificarPersona("X", "Y"));

        evento.eliminarCharlasSpeaker("123");

        evento.ordenarCharlasPorParticipantes();
        evento.mostrarCharlas();
    }
}
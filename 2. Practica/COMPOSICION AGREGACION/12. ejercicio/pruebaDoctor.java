
public class pruebaDoctor {
    public static void main(String[] args) {
        Doctor d1 = new Doctor("Dr1", "Cardiologia");
        Doctor d2 = new Doctor("Dr2", "Neurologia");

        Hospital h1 = new Hospital("Hospital1", 10);
        Hospital h2 = new Hospital("Hospital2", 10);

        h1.asignarDoctor(d1);
        h1.asignarDoctor(d2);
        h2.asignarDoctor(d1); 

        h1.mostrarDoctores();
        h2.mostrarDoctores();
    }
}

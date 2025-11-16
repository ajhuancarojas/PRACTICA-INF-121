
public class pruebaFarmacia {
    public static void main(String[] args) {
        Farmacia f = new Farmacia("Farmacia Chavez", "Calle 21");

        Medicamento med1 = new Medicamento("Aspirina", 10.5, 5);
        med1.agregarRegistro(new Registro("2025-11-10", 98));
        med1.agregarRegistro(new Registro("2025-11-15", 75));

        f.agregarMedicamento(med1);

        f.mostrar();
    }
}
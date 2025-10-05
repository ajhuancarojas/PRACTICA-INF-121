package polimorfismo;
public class testparada {
    public static void main(String[] args) {
        Parada p = new Parada("Parada Central");

        p.adicionar("carla hurtado");
        p.adicionar("TOYOTA", "manuel", "123ABC");
        p.adicionar("SUSUKI", "erika", "456XYZ");
        p.mostrar();
    }
}

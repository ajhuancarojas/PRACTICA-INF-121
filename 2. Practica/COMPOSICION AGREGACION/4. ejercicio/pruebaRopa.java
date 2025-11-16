
public class pruebaRopa{
    public static void main(String[] args) {
        Ropero r = new Ropero("Madera");
      
        r.adicionarPrenda(new Ropa("Camisa", "poliester"));
        r.adicionarPrenda(new Ropa("Pantalon", "Jeans"));
        r.adicionarPrenda(new Ropa("Camisa", "tela"));

        r.mostrarPrendas("Algodon", "Camisa");

        r.eliminarPrendas("Algodon");
        r.eliminarPrendas("Pantalon");
        r.mostrarPrendas("tela", "Camisa");
    }
}
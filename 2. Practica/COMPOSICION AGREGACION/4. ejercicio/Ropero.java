
public class Ropero {
    private String material;
    private Ropa[] ropas;
    private int nroRopas;

    public Ropero(String material) {
        this.material = material;
        this.ropas = new Ropa[20];
        this.nroRopas = 0;
    }

    public void adicionarPrenda(Ropa r) {
        if (nroRopas < 20) {
            ropas[nroRopas++] = r;
        }
    }

    public void eliminarPrendas(String criterio) {
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getMaterial().equals(criterio) || ropas[i].getTipo().equals(criterio)) {
                for (int j = i; j < nroRopas - 1; j++) {
                    ropas[j] = ropas[j + 1];
                }
                nroRopas--;
                i--; 
            }
        }
    }

    public void mostrarPrendas(String material, String tipo) {
        System.out.println("Prendas en ropero de " + this.material + " con material " + material + " y tipo " + tipo + ":");
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getMaterial().equals(material) && ropas[i].getTipo().equals(tipo)) {
                System.out.println(" - Tipo: " + ropas[i].getTipo() + ", Material: " + ropas[i].getMaterial());
            }
        }
        System.out.println();
    }
}
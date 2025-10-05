package polimorfismo;
public class testMatriz {
   public static void main(String[] args) {
        Matriz x = new Matriz();
        System.out.println("Matriz Identidad:");
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.printf("%6.1f ", x.getMatriz()[i][j]);
            }
            System.out.println();
        }
        float[][] d = new float[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                d[i][j] = i + j;
            }
        }
        Matriz m2 = new Matriz(d);
        System.out.println(" m2:");
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.printf("%6.1f ", m2.getMatriz()[i][j]);
            }
            System.out.println();
        }
        Matriz s = x.sumar(m2);
        System.out.println("\nSuma:");
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.printf("%6.1f ", s.getMatriz()[i][j]);
            }
            System.out.println();
        }
        Matriz r = x.restar(m2);
        System.out.println("\nResta:");
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.printf("%6.1f ", r.getMatriz()[i][j]);
            }
            System.out.println();
        }
        System.out.println("\nSon iguales....? " + x.igual(m2));
    }
}

package polimorfismo;
public class Matriz {
    private float[][] m = new float[10][10];
    public Matriz() {
        for (int i = 0; i < 10; i++) {
            m[i][i] = 1.0f;
        }
    }
    public Matriz(float[][] m) {
        this.m = (m.length == 10 && m[0].length == 10) ? m : new Matriz().m;
    }
    public float[][] getMatriz() {
        return m;
    }
    public Matriz sumar(Matriz otra) {
        float[][] resultado = new float[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado[i][j] = this.m[i][j] + otra.m[i][j];
            }
        }
        return new Matriz(resultado);
    }

    public Matriz restar(Matriz otra) {
        float[][] r = new float[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                r[i][j] = this.m[i][j] - otra.m[i][j];
            }
        }
        return new Matriz(r);
    }
    public boolean igual(Matriz otra) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (this.m[i][j] != otra.m[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    
}

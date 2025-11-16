+
public class NumeroInvalidoException extends Exception {
    public NumeroInvalidoException(String msg) {
        super(msg);
    }
}
class Calculadora {
    public static double sumar(double a, double b) {
        return a + b;
    }

    public static double restar(double a, double b) {
        return a - b;
    }

    public static double multiplicar(double a, double b) {
        return a * b;
    }

    public static double dividir(double a, double b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("División por cero");
        }
        return a / b;
    }

    public static int stringToInt(String s) throws NumeroInvalidoException {
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {
            throw new NumeroInvalidoException("No es un número válido");
        }
    }
}
 
class prueba {
    public static void main(String[] args) {
        
        System.out.println("Suma: " + Calculadora.sumar(5, 3));
        System.out.println("Resta: " + Calculadora.restar(5, 3));
        System.out.println("Multi: " + Calculadora.multiplicar(5, 3));
        try {
            System.out.println("Div: " + Calculadora.dividir(5, 3));
            System.out.println("ToInt: " + Calculadora.stringToInt("10"));
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        try {
            Calculadora.dividir(5, 0);
        } catch (ArithmeticException e) {
            System.out.println("Error div: " + e.getMessage());
        }
        try {
            Calculadora.stringToInt("abc");
        } catch (NumeroInvalidoException e) {
            System.out.println("Error toInt: " + e.getMessage());
        }
    }
}
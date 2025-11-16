
public class FondosInsuficientesException extends Exception {
    public FondosInsuficientesException(String msg) {
        super(msg);
    }
}

 class CuentaBancaria {
    private String numeroCuenta;
    private String titular;
    private double saldo;

    public CuentaBancaria(String numeroCuenta, String titular, double saldo) {
        this.numeroCuenta = numeroCuenta;
        this.titular = titular;
        this.saldo = saldo;
    }

    public void depositar(double monto) {
        if (monto <= 0) {
            throw new IllegalArgumentException("Monto negativo o cero");
        }
        saldo += monto;
    }

    public void retirar(double monto) throws FondosInsuficientesException {
        if (monto > saldo) {
            throw new FondosInsuficientesException("Fondos insuficientes");
        }
        saldo -= monto;
    }

    public void mostrarInfo() {
        System.out.println("Cuenta: " + numeroCuenta + ", Titular: " + titular + ", Saldo: " + saldo);
    }
}

class correr {
    public static void main(String[] args) {

        CuentaBancaria cuenta = new CuentaBancaria("12345", "Juan Pérez", 1000);

        try {
            cuenta.depositar(500);
            cuenta.mostrarInfo();
            cuenta.depositar(-100);
        } catch (IllegalArgumentException e) {
            System.out.println("Error depósito: " + e.getMessage());
        }

        try {
            cuenta.retirar(200); 
            cuenta.mostrarInfo();
            cuenta.retirar(2000); 
        } catch (FondosInsuficientesException e) {
            System.out.println("Error retiro: " + e.getMessage());
        }
    }
}
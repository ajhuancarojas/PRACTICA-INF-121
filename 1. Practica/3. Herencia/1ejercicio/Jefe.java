package Herencia;
public class Jefe extends Persona {
    private String sucursal;
    private String tips;
    public Jefe(String sucursal, String tips, String CI, String nombre, String apellido) {
        super(nombre, apellido, CI); 
        this.sucursal = sucursal;
        this.tips = tips;
    }
public Jefe(String sucursal, String tips, String CI) {
        super(CI); 
        this.sucursal = sucursal;
        this.tips = tips;
    }
}

 
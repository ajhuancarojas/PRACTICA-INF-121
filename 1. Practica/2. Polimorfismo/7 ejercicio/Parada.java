
package polimorfismo;
public class Parada {
    private String[] admins = new String[10];
    private String[][] autos = new String[10][3];
    private String nombreP;
    private int nroAdmins;
    private int nroAutos;
    public Parada() {
        this.nombreP = "Sin nombre";
        this.nroAdmins = 0;
        this.nroAutos = 0;
    }
    public Parada(String nombreP) {
        this.nombreP = nombreP;
        this.nroAdmins = 0;
        this.nroAutos = 0;
    }
    public void mostrar() {
        System.out.println("Parada: " + nombreP);
        System.out.println("Administradores:");
        for (int i = 0; i < nroAdmins; i++) {
            System.out.println(" - " + admins[i]);
        }

        System.out.println("Autos:");
        for (int i = 0; i < nroAutos; i++) {
            System.out.println("Modelo: " + autos[i][0] );
            System.out.println("Conductor: " + autos[i][1]);
            System.out.println("Placa: " + autos[i][2]);
        }
    }
    public void adicionar(String admin) {
        if (nroAdmins < admins.length) {
            admins[nroAdmins] = admin;
            nroAdmins++;
        } else {
            System.out.println("No se pueden agregar ms adm");
        }
    }
    public void adicionar(String modelo, String conductor, String placa) {
        if (nroAutos < autos.length) {
            autos[nroAutos][0] = modelo;
            autos[nroAutos][1] = conductor;
            autos[nroAutos][2] = placa;
            nroAutos++;
        } else {
            System.out.println("No se pueden agregar mas autos");
        }
    }

    
}


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Herencia;

class Cliente extends Persona {
    private String randompza;
    private String ticCliente;

    public Cliente(String nombre, String apellido, String CI, String randompza, String ticCliente) {
        super(nombre, apellido, CI);
        this.randompza = randompza;
        this.ticCliente = ticCliente;
    }
}

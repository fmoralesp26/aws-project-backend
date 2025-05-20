package com.example.conversor_moeda.moeda;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Table;
import jakarta.persistence.Id;

@Entity
@Table(name="moeda")
public class Moeda {

    @Id 
    @GeneratedValue
    private Long id;
    
    private String pais;
    private double valor;

    public Moeda(String pais, double valor) {
        this.pais = pais;
        this.valor = valor;
    }

    public Moeda() {}

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    
}

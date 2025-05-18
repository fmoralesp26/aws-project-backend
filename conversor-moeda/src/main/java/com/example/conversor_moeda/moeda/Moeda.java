package com.example.conversor_moeda.moeda;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Table;

@Entity
@Table(name="empresas")
public class Moeda {

    @GeneratedValue
    private Long id;

    private String pais;
    private double valor;

    public Moeda(String pais, double valor) {
        this.pais = pais;
        this.valor = valor;
    }

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

package com.example.conversor_moeda.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;

@CrossOrigin(origins = "http://44.204.219.241:8080")
@RestController
public class MoedaController {

    @GetMapping("/conversao")
    public double converter(@RequestParam String para, @RequestParam double valor) {
        double taxaConversao = getTaxaConversao(para);
        return valor * taxaConversao;
    }

    private double getTaxaConversao(String para) {
        switch (para) {
            case "dolares" -> {
                return 0.19; 
            }
            case "euros" -> {
                return 0.18; 
            }
            case "libras" -> {
                return 0.15; 
            }
            case "iens" -> {
                return 25.00; 
            }
            case "francos" -> {
                return 0.17; 
            }
            case "dirhans" -> {
                return 0.65; 
            }
            case "pesos" -> {
                return 38.00; 
            }
            default -> throw new IllegalArgumentException("Moeda não suportada: " + para);
        }
    }
}

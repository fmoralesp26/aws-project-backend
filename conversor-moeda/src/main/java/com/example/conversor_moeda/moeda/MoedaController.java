package com.example.conversor_moeda.moeda;

import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.Optional;

@CrossOrigin(origins = "http://44.204.219.241:8080")
@RestController
public class MoedaController {

    @Autowired
    private MoedaRepo moedaRepo;

    public MoedaController() {
    }

    // GET /moeda 
    @GetMapping("/moeda")
    public Iterable<Moeda> getMoedas() {
        return moedaRepo.findAll();
    }

    // GET /moeda/{pais} 
    @GetMapping("/moeda/{pais}")
    public Moeda getMoedaByPais(@PathVariable String pais) {
        return moedaRepo.findByPaisIgnoreCase(pais)
                .orElseThrow(() -> new IllegalArgumentException("Moeda para o país '" + pais + "' não encontrada."));
    }

    // GET /moeda/converter/{pais}?valor=100.0
    @GetMapping("/moeda/converter/{pais}")
    public double getConversao(@PathVariable String pais, @RequestParam double valor) {
        Moeda moeda = moedaRepo.findByPaisIgnoreCase(pais)
                .orElseThrow(() -> new IllegalArgumentException("Moeda para o país '" + pais + "' não encontrada no banco de dados."));

        return valor * moeda.getValor();
    }
}

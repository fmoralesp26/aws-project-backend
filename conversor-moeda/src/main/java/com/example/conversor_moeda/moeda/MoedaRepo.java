package com.example.conversor_moeda.moeda;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

public interface MoedaRepo extends CrudRepository<Moeda, Long> {
    Optional<Moeda> findByPaisIgnoreCase(String pais);
}

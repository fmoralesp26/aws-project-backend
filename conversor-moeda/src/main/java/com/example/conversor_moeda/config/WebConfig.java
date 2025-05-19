package com.example.conversor_moeda.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**") 
                .allowedOrigins("**")  // Permite todas as origens
                .allowedMethods("GET", "POST", "PUT", "DELETE") 
                .allowedHeaders("*")  // Permite todos os cabeçalhos
                .allowCredentials(true); // Permite credenciais (como cookies)
    }
}

CREATE TABLE locatario (
  id_locatario int PRIMARY KEY
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  orcamento_maximo decimal(12,2),
  raio_busca_km decimal(6,2),
  limiar_compatibilidade int,
  preferencias_moradia jsonb
);
CREATE TABLE imovel (
  id_imovel SERIAL PRIMARY KEY,
  id_locador int NOT NULL
    REFERENCES locador (id_locador) DEFERRABLE INITIALLY IMMEDIATE,
  valor_aluguel decimal(12,2),
  valor_condominio decimal(12,2),
  valor_iptu decimal(12,2),
  valor_contas_extras decimal(12,2),
  tipo_imovel varchar(50),
  quantidade_quartos int,
  vagas_disponiveis int,
  area_m2 decimal(10,2),
  descricao text,
  caracteristicas jsonb,
  status_disponibilidade varchar(30) NOT NULL,
  data_cadastro timestamptz NOT NULL
);
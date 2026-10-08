CREATE TABLE morador_imovel (
  id_morador_imovel BIGSERIAL PRIMARY KEY,
  id_usuario int NOT NULL
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  id_imovel int NOT NULL
    REFERENCES imovel (id_imovel) DEFERRABLE INITIALLY IMMEDIATE,
  data_entrada date,
  data_saida date,
  status_moradia varchar(30) NOT NULL
);

CREATE UNIQUE INDEX ON morador_imovel (id_usuario, id_imovel);
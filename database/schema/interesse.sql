CREATE TABLE interesse (
  id_interesse BIGSERIAL PRIMARY KEY,
  id_usuario int NOT NULL
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  id_imovel int NOT NULL
    REFERENCES imovel (id_imovel) DEFERRABLE INITIALLY IMMEDIATE,
  tipo_interesse varchar(20) NOT NULL,
  data_interesse timestamptz NOT NULL
);

CREATE UNIQUE INDEX ON interesse (id_usuario, id_imovel);
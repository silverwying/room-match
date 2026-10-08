CREATE TABLE conversa (
  id_conversa SERIAL PRIMARY KEY,
  id_imovel int NOT NULL
    REFERENCES imovel (id_imovel) DEFERRABLE INITIALLY IMMEDIATE,
  data_criacao timestamptz NOT NULL,
  status_conversa varchar(30) NOT NULL
);
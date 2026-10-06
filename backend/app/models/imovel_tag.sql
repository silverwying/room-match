CREATE TABLE imovel_tag (
  id_imovel int
    REFERENCES imovel (id_imovel) DEFERRABLE INITIALLY IMMEDIATE,
  id_tag int
    REFERENCES tag (id_tag) DEFERRABLE INITIALLY IMMEDIATE,
  PRIMARY KEY (id_imovel, id_tag)
);
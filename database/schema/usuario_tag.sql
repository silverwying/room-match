CREATE TABLE usuario_tag (
  id_usuario int
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  id_tag int
    REFERENCES tag (id_tag) DEFERRABLE INITIALLY IMMEDIATE,
  PRIMARY KEY (id_usuario, id_tag)
);
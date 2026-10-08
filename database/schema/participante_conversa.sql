CREATE TABLE participante_conversa (
  id_conversa int
    REFERENCES conversa (id_conversa) DEFERRABLE INITIALLY IMMEDIATE,
  id_usuario int
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  data_entrada timestamptz NOT NULL,
  PRIMARY KEY (id_conversa, id_usuario)
);
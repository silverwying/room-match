CREATE TABLE mensagem (
  id_mensagem BIGSERIAL PRIMARY KEY,
  id_conversa int NOT NULL
    REFERENCES conversa (id_conversa) DEFERRABLE INITIALLY IMMEDIATE,
  id_remetente int NOT NULL
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  conteudo text NOT NULL,
  data_envio timestamptz NOT NULL,
  status_leitura varchar(30) NOT NULL
);		
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS VetorRandomizado (
    id INTEGER PRIMARY KEY NOT NULL,
    vetor_values TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS VetorRandomizadoDescricao (
    id_vetor_randomizado INTEGER NOT NULL,
    nome_vetor TEXT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_vetor_randomizado) REFERENCES VetorRandomizado(id)
);
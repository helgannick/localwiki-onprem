CREATE DATABASE IF NOT EXISTS localwiki;
USE localwiki;

CREATE TABLE artigos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    conteudo TEXT,
    autor VARCHAR(100),
    data DATETIME
);

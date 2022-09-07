select * from curriculo;

-- Atuacao
INSERT INTO atuacao VALUES
(DEFAULT, 'Progamador Júnior', '1', '1');

INSERT INTO empregosanteriores VALUES
(DEFAULT, 'Estagiario DEV', '2');


select * from atuacao;
select * from empregosanteriores;

DESC atuacao;
DESC __area_atuacao;
DESC empregosanteriores;

-- Projetos
SELECT * FROM projetos;
SELECT * FROM projetosemandamento;
SELECT * FROM projetosterminados;
SELECT * FROM projeto;

DESC projetos;
DESC projetosemandamento;
DESC projetosterminados;
DESC projeto;

INSERT INTO projeto VALUES 
(
DEFAULT,
'A Importância da Matemática Financeira no Cotidiano',
'Esse projeto busca compreender como a matemática financeira é abordada nas escolas, além de compreender a aplicação de conceitos básicos de matemática para finanças pessoais.',
'40',
'Pesquisa',
'Sheila Chrisley de Assis'
);
INSERT INTO projeto VALUES 
(
DEFAULT,
'Matemática Financeira: Um desafio para além dos muros do IFC - Campus Concórdia',
'Esse projeto busca compreender como a matemática financeira é abordada nas escolas, além de compreender a aplicação de conceitos básicos de matemática para finanças pessoais.',
'40',
'Extensão',
'Sheila Chrisley de Assis'
);

INSERT INTO projetosterminados values (1, '2021-01-01', '2021-09-01', '16');
INSERT INTO projetosemandamento values (1, '2022-03-01', '17');

INSERT INTO projetos VALUES (DEFAULT, null, 1);

SELECT * FROM projetosemandamento;
SELECT * FROM projetos;
select * from projeto;

-- CURRICULO
INSERT INTO curriculo VALUES (
DEFAULT,
'Jucian Kauê Decezare',
'098.543.654-12',
'49989140512',
'jucian_decezare2015@hotmail.com',
'Hi, my name is Jucian',
'2022-09-02',
'1',
'2',
'1'
);

select * from formacao;
SELECT * FROM atuacao;
SELECT * FROM projetos;
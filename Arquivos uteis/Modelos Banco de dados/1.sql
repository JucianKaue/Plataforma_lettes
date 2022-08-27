SELECT * FROM site_lettes.__nivel_ensino;
DELETE FROM __nivel_ensino WHERE id = 0; 
INSERT INTO __nivel_ensino VALUES (
	2, 'Ensino Fundamental Completo'
);

INSERT INTO cursos VALUES (
	DEFAULT, 'HTML4', 'Um curso top de HTML5', 30, '', 'Curso em Vio'
);
select * from cursos;
INSERT INTO formacao VALUES (
	DEFAULT, '1', 4, 'Nada'
);

INSERT INTO formacao_has_cursos VALUES (
	1, 4
);

INSERT INTO projeto VALUES (
	DEFAULT, 'Projetin Fellas', 'Maromba em 3 horas semanais', '20', 1, DEFAULT
);


USE site_lettes;
SELECT * FROM formacao_has_cursos;
SELECT * FROM formacao;
SELECT * FROM cursos;


-- SELECT formação
SELECT formacao.id, __nivel_ensino.nivel, cursos.nome, formacao.complemento FROM Formacao 
JOIN formacao_has_cursos ON formacao.cursos = formacao_has_cursos.formação_id 
JOIN cursos ON formacao_has_cursos.cursos_id = cursos.id 
JOIN __nivel_ensino ON formacao.nivel_ensino = __nivel_ensino.id;

SELECT * FROM Projetos
JOIN projetosemandamento ON projetosemandamento.id = Projetos.projetosemandamento
JOIN projeto ON projeto.projetosemandamento = projetosemandamento.id;

desc curriculo;





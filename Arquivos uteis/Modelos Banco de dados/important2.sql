SELECT * from users;
SELECT * FROM users where username = 'Jucian';

delete FROM users WHERE password = '123' limit 1;

UPDATE users SET ip = '' WHERE username = 'Jucian' limit 1;
UPDATE users SET ip = '127.0.0.1' WHERE username = 'Jucian' limit 1;
UPDATE users SET ip = Null WHERE username = 'jucian' limit 1;

-- FORMAÇÃO
SELECT formacao.id, __nivel_ensino.nivel, cursos.nome, formacao.complemento FROM Formacao 
JOIN formacao_has_cursos ON formacao.cursos = formacao_has_cursos.formação_id 
JOIN cursos ON formacao_has_cursos.cursos_id = cursos.id 
JOIN __nivel_ensino ON formacao.nivel_ensino = __nivel_ensino.id;

-- ATUAÇÃO
SELECT a.empregoatual, _area.name, e.nome FROM atuacao a JOIN empregosanteriores e ON a.id = e.Atuacao JOIN __area_atuacao _area ON a.__area_atuacao = _area.id;

-- PROJETOS EM ANDAMENTO
SELECT proj.id, proj_.projeto_id, projeto.nome  FROM projetos proj
JOIN projetosemandamento proj_ on proj.projetosemandamento = proj_.id
JOIN projeto ON proj_.projeto_id = projeto.id;

-- PROJETOS TERMINADOS
SELECT proj.id, proj_.projeto_id, projeto.nome FROM projetos proj
JOIN projetosterminados  proj_ ON proj.projetosterminados = proj_.id
JOIN projeto ON proj_.projeto_id = projeto.id;

SELECT * FROM curriculo JOIN formacao on formacao.id = ;
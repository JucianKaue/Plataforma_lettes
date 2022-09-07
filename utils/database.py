import datetime
import mysql.connector

database_padrao = 'Site_lettes'

class Curriculo:
    def __init__(self, idcurriculo, nome, CPF, telefone, email, resumo, ultimaatualizacao, formacao, atuacao, projetos):
        self._idcurriculo = idcurriculo
        self._imagem = CPF
        self._nome = nome
        self._cpf = CPF
        self._telefone = telefone
        self._email = email
        self._resumo = resumo
        self._ultimaatualizacao = ultimaatualizacao
        self._formacao = formacao
        self._atuacao = atuacao
        self._projetos = projetos


    @staticmethod
    def get_curriculo_by_id(id):
        db_result = mysql_select('curriculo', filtros={'idcurriculo': f'{id}'})

        print(db_result)


class Users:
    def __init__(self, usuario=str, email=str, senha=str, date=str, curriculo=Curriculo):
        self._usuario = usuario
        self._email = email
        self._senha = senha
        self._date = date
        self._curriculo = curriculo


class Formacao:
    def __init__(self, ensino=str, cursos=list, complemento=str):
        self._ensino = ensino
        self._cursos = cursos
        self._complemento = complemento


class Curso:
    def __init__(self, nome=str, descricao=str, cargahoraria=int, certificado=str, instituicao=str):
        self._nome = nome
        self._descricao = descricao
        self._cargahoraria = cargahoraria
        self._certificado = certificado
        self._instituicao = instituicao


class Projetos:
    def __init__(self, projetosandamento=list, projetosterminados=str):
        self._projetosandamento = projetosandamento
        self._projetosterminados = projetosterminados


class Projeto:
    def __init__(self, nome=str, descricao=str, coordenador=str, cargahoraria=int, data_inicio=datetime.date, data_fim=datetime.date):
        self._nome = nome
        self._descricao = descricao
        self._coordenador = coordenador
        self._cargahoraria = cargahoraria
        self._datas = {'inicio': data_inicio, 'fim': data_fim}


class Atuacao:
    def __init__(self, id=int, area=str, empregoatual=str, empregos=list):
        self._id = id
        self._area = area
        self._empregoatual = empregoatual
        self._empregosanteriores = empregos


def mysql_connect():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="")


def mysql_command(sql, fetch=False):
    db = mysql_connect()
    c = db.cursor()
    c.execute(f"USE {database_padrao}")
    c.execute(f"{sql}")
    db.commit()
    if fetch:
        return c.fetchall()
    else:
        return f"{c.rowcount} rows affected"


def mysql_insert(table, data):
    k, v, values = '', '', []
    sql = f'INSERT INTO {table} ('
    for key in data.keys():
        k += f'`{key}`, '
        v += f'%s, '
        values.append(f'{data[f"{key}"]}')
    sql += f"{k[:-2]}) VALUES ({v[:-2]});"

    db = mysql_connect()
    c = db.cursor()
    c.execute(f"USE {database_padrao}")
    c.execute(sql, values)
    db.commit()
    return f"{c.rowcount} rows affected"


def mysql_select(table=str(' '), columns=list([]), filtros=dict({})):
    sql = "SELECT "
    if len(columns) > 0:
        for c in columns:
            sql += f'{c}, '
        sql = f"{sql[:-2]}"
    else:
        sql += '*'

    sql += f" FROM {table}"
    if len(filtros.keys()) > 0:
        sql += ' WHERE '
        for k in filtros.keys():
            sql += F"{k} = '{filtros[k]}' AND "
        sql = f"{sql[:-5]}"
    sql += ';'

    print(sql)

    db = mysql_connect()
    c = db.cursor()
    c.execute(f'USE {database_padrao};')
    c.execute(f"{sql}")
    return c.fetchall()


def mysql_get_curriculo(id):
    db = mysql_connect()
    c = db.cursor(buffered=True)
    c.execute(f"USE {database_padrao}")
    c.execute(f"SELECT id, nome, telefone, ultimaatualizacao, resumo FROM curriculo WHERE curriculo.id = {id};")
    geral = c.fetchall()
    c.execute(f"SELECT __nivel_ensino.nivel, cursos.nome, cursos.cargahoraria, cursos.descricao, cursos.instituição, Formacao.complemento FROM curriculo JOIN formacao on formacao.id = curriculo.Formacao JOIN formacao_has_cursos ON formacao.cursos = formacao_has_cursos.formação_id JOIN cursos ON formacao_has_cursos.cursos_id = cursos.id JOIN __nivel_ensino ON formacao.nivel_ensino = __nivel_ensino.id WHERE curriculo.id = {id};")
    formacao = c.fetchall()

    cursos = []
    for curso in formacao:
        cursos.append(Curso(
            nome=curso[1],
            cargahoraria=curso[2],
            descricao=curso[3],
            instituicao=curso[4]
        ))

    c.execute(f"SELECT atuacao.id, atuacao.empregoatual, empregosanteriores.nome, __area_atuacao.name FROM curriculo JOIN atuacao ON curriculo.atuacao = atuacao.id JOIN empregosanteriores ON empregosanteriores.atuacao = atuacao.empregos JOIN __area_atuacao ON atuacao.__area_atuacao = __area_atuacao.id WHERE curriculo.id = {id};")
    atuacao = c.fetchall()

    empregosanteriores = []
    for a in atuacao:
        empregosanteriores.append(a[2])

    c.execute(f"SELECT projeto.nome, projeto.descricao, projeto.cargahoraria, projeto.natureza, projeto.coordenadores, proj_.datainicio, proj_.datatermino FROM curriculo JOIN projetos proj ON curriculo.projetos = proj.id JOIN projetosterminados proj_ on proj.projetosterminados = proj_.id JOIN projeto ON proj_.projeto_id = projeto.id WHERE curriculo.id = {id};")
    projetos_terminados_list = c.fetchall()
    projetos_terminados = []
    for projeto_t in projetos_terminados_list:
        projetos_terminados.append(Projeto(
            nome=projeto_t[0],
            descricao=projeto_t[1],
            coordenador=projeto_t[4],
            cargahoraria=projeto_t[2],
            data_inicio=projeto_t[5],
            data_fim=projeto_t[6]
        ))

    c.execute(f"SELECT projeto.nome, projeto.descricao, projeto.cargahoraria, projeto.natureza, projeto.coordenadores, proj_.datainicio FROM curriculo JOIN projetos proj ON curriculo.projetos = proj.id JOIN projetosemandamento proj_ on proj.projetosemandamento = proj_.id JOIN projeto ON proj_.projeto_id = projeto.id WHERE curriculo.id = {id};")
    projetos_andamento_list = c.fetchall()
    projetos_andamento = []
    for projeto_a in projetos_andamento_list:
        projetos_andamento.append(Projeto(
            nome=projeto_a[0],
            descricao=projeto_a[1],
            coordenador=projeto_a[4],
            cargahoraria=projeto_a[2],
            data_inicio=projeto_a[5]
        ))

    curriculo = Curriculo(
        idcurriculo=geral[0][0],
        nome=f'{geral[0][1]}',
        telefone=geral[0][2],
        ultimaatualizacao=geral[0][3],
        resumo=geral[0][4],
        CPF=None,
        email=None,
        formacao=Formacao(
            ensino=formacao[0][0],
            cursos=cursos,
            complemento=formacao[0][5]
        ),
        atuacao=Atuacao(
            id=atuacao[0][0],
            empregoatual=atuacao[0][1],
            empregos=empregosanteriores,
            area=atuacao[0][3]
        ),
        projetos=Projetos(
            projetosandamento=projetos_andamento,
            projetosterminados=projetos_terminados
        )
    )

    print(geral, cursos[0]._instituicao)

    return curriculo

import mysql.connector

database_padrao = 'mydb'


class Curriculo:
    def __init__(self, nome, CPF, telefone, email, resumo, ultimaatualizacao, formacao, atuacao, projetos):
        self._idcurriculo = 'DEFAULT'
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
    def __init__(self, nome=str, descricao=str, cargahoraria=int, certificado=str, criador_curso=str):
        self._nome = nome
        self._descricao = descricao
        self._cargahoraria = cargahoraria
        self._certificado = certificado
        self._criadorcurso = criador_curso


class Projetos:
    def __init__(self, id=int, projetosandamento=list, projetosterminados=str):
        self._id = id
        self._projetosandamento = projetosandamento
        self._projetosterminados = projetosterminados


class Projeto:
    def __init__(self, nome=str, descricao=str, cargahoraria=int):
        self._nome = nome
        self._descricao = descricao
        self._cargahoraria = cargahoraria


class Atuacao:
    def __init__(self, id=int, area=str, empregoatual=str, empregos=list):
        self._id = id
        self._area = area
        self._empregoatual = empregoatual
        self._empregosanteriores = empregos


def mysql_connect():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="")


def mysql_command(sql):
    db = mysql_connect()
    c = db.cursor()
    c.execute(f"USE {database_padrao}")
    c.execute(f"{sql}")
    return c.fetchall()


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
            sql += F'{k} = {filtros[k]} AND '
        sql = f"{sql[:-5]};"
    else:
        sql += ';'

    print(sql)

    db = mysql_connect()
    c = db.cursor()
    c.execute(f'USE {database_padrao};')
    c.execute(f"{sql}")
    return c.fetchall()



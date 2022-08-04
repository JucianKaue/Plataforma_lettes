import mysql.connector


class Curriculo:
    def __init__(self, id, nome, CPF, telefone, email, resumo, ultimaatualizacao, formacao, atuacao, projetos):
        self._idcurriculo = id
        self._nome = nome
        self._cpf = CPF
        self._telefone = telefone
        self._email = email
        self._resumo = resumo
        self._ultimatualizacao = ultimaatualizacao
        self._formacao = formacao
        self._atuacao = atuacao
        self._projetos = projetos


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


class Cursos:
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
    mysql_connect().cursor(sql).execute(f"{sql}")


def mysql_insert(sql, values):
    mysql_connect().cursor(sql).execute(f"{sql}", values)


def mysql_select(sql):
    return mysql_connect().cursor(sql).execute(f"{sql}").fetchall()


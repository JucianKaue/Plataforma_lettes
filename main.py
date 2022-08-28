import datetime

from flask import Flask, render_template, request, redirect, url_for
from utils.database import *

app = Flask(__name__)

c = Curriculo(
    nome='Jucian Kauê Decezare',
    CPF='032.654.765-23',
    telefone='49989140512',
    email='juciandecezare@hotmail.com',
    resumo='Hello, my name is Jucian',
    ultimaatualizacao='Today',
    formacao=None,
    atuacao=Atuacao(
        id=1,
        area='Ciencia da computaria',
        empregoatual='Cientista de porra nenhuma',
        empregos=['EU NUNCA TABALHEI PORRA']
    ),
    projetos=Projetos(
        id=1,
        projetosandamento=[Projeto(
            nome='DDoS do pellas',
            descricao='cansei da vida',
            cargahoraria=1
        )],
        projetosterminados=[Projeto(
            nome='Dormir',
            descricao='Estou com sono',
            cargahoraria=20
        )]
    ))


@app.route('/')
def main():
    username = mysql_select('users', ['username'], filtros={'ip': request.environ['REMOTE_ADDR']})
    if username: username = username[0][0]
    return render_template('Curriculo.html', title='WELCOME', curriculo=c, username=username)


@app.route('/adicionarcurriculo', methods=['GET', 'POST'])
def AddCurriculo():
    if request.method == 'GET':
        return render_template('AddCurriculo.html', form_variaveis={
            'niveis_ensino': mysql_select('__nivel_ensino'),
            'areas_atuacao': mysql_select('__area_atuacao')
        })
    elif request.method == 'POST':

        # Formulário projeto
        if f"{request.form.keys()}" == "dict_keys(['nome_projeto', 'descricao_projeto', 'cargahoraria_Projeto', 'datainicio_Projeto', 'datafim_Projeto'])":
            p = Projeto(
                nome=request.form.get('nome_projeto'),
                descricao=request.form.get('descricao_projeto'),
                cargahoraria=request.form.get('cargehoraria_Projeto'),
                data_inicio=request.form.get('datainicio_Projeto'),
                data_fim=request.form.get('datafim_Projeto')
            )
            # Chamar função para salvar no banco de dados

        # Formulário Curso
        elif f"{request.form.keys()}" == "dict_keys(['nome_curso', 'descricao_curso', 'cargahoraria_curso', 'instituicao_curso', 'certificado_curso'])":
            c = Curso(
                nome=request.form.get('nome_curso'),
                descricao=request.form.get("descricao_curso"),
                cargahoraria=request.form.get("cargahoraria_curso"),
                instituicao=request.form.get("instituicao_curso"),
                certificado='??' #DESCOBRIR O Q CARALHOS FZR AQ
            )

            mysql_insert('cursos', {
                'id': 'DEFAULT',
            })

        else:
            nome = request.form.get('nome')
            cpf = request.form.get('CPF')
            telefone = request.form.get('telefone')
            email = request.form.get('email')
            resumo = request.form.get('resumo')

            formacao = request.form.get('formacao')[0]
            cursos = "AINDA N SEI COMO FAZER ESSA PORRA"
            complemento = request.form.get('complemento_textarea')

            projetos_andamento = "EU SEI LA"
            projetos_finalizados = "sei lá porra"

            area_atuacao = request.form.get('area_atuacao_select')
            emprego_atual = request.form.get('emprego_input')
            empregos_passados = ['n sei']

            return f"{formacao}"


@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html', title='Login')
    elif request.method == 'POST':
        user = {
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'ip': request.environ['REMOTE_ADDR']
        }
        user_db = mysql_select('users', filtros={'username': user['username'], 'password': user['password']})
        if user_db:
            mysql_command(f"UPDATE users SET ip = '{user['ip']}' WHERE username = '{user['username']}' limit 1;")
        else:
            return f'Usuário ou senha incorretos'

        return redirect(url_for('main'))


@app.route('/logout')
def Logout():
    mysql_command(f"UPDATE users SET ip = Null WHERE ip = '{request.environ['REMOTE_ADDR']}' limit 1;")
    return redirect(url_for('main'))



@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method == 'GET':
        return render_template('Cadastro.html', title='Cadastro')
    elif request.method == 'POST':
        if request.form.get('password') != request.form.get('password_confirm'):
            return "SENHAS NÃO COINCIDEM"
        if mysql_select('users', filtros={'username': request.form.get('username')}):
            return "Esse nome de usuário já está registrado."
        if mysql_select('users', filtros={'email': request.form.get('email')}):
            return "Esse email está logado."

        user = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'createdate': f"{datetime.datetime.today().year}-{datetime.datetime.today().month:0>2}-{datetime.datetime.today().day:0>2}"
        }

        try:
            mysql_insert('users', user)
            return redirect(url_for('Login'))
        except:
            return 'Um erro inesperado ocorreu durante a utilização do banco de dados.'


if __name__ == '__main__':
    app.run(debug=True)

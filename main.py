from flask import Flask, render_template, request
from utils.database import *

app = Flask(__name__)

c = Curriculo(
    nome='Jucian Kauê Decezare',
    CPF='032.654.765-23',
    telefone='49989140512',
    email='juciandecezare@hotmail.com',
    resumo='Hello, my name is Jucian',
    ultimaatualizacao='Today',
    formacao=True,
    atuacao=Atuacao(
        id=1,
        area='Ciencia da computaria',
        empregoatual='Cientista de porra nenhuma',
        empregos=['EU NUNCA TABALHEI PORRA']
    ),
    projetos=Projetos(
        id=1,
        projetosandamento=[
            Projeto(
                nome='DDoS do pellas',
                descricao='cansei da vida',
                cargahoraria=1
            )
        ],
        projetosterminados=[
            Projeto(
                nome='Dormir',
                descricao='Estou com sono',
                cargahoraria=20
            )
        ]
    )
)


@app.route('/')
def main():
    return render_template('Curriculo.html', title='WELCOME', curriculo=c)


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


if __name__ == '__main__':
    app.run(debug=True)

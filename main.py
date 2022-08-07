from flask import Flask, render_template
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
    return render_template('index.html', title='WELCOME', curriculo=c)


@app.route('/adicionarcurriculo', methods=['GET', 'POST'])
def AddCurriculo(request):
    if request.method == 'GET':
        return render_template('AddCurriculo.html', form_variaveis={
            'niveis_ensino': mysql_select('__niveis_ensino'),
            'areas_atuacao': mysql_select('__areas_atuacao')
        })
    elif request.method == 'POST':
        nome = request.form['input_nome']
        print(nome)


if __name__ == '__main__':
    app.run(debug=True)

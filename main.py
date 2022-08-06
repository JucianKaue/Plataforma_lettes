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
    formacao=Formacao(
        ensino='Ensino Médio Completo',
        cursos=[Curso(
            nome='HTML5',
            descricao='Um curso de html 5',
            cargahoraria=40,
            certificado='oi',
            criador_curso='Estudonauta'
        )],
        complemento='Nothing'
    ),
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
    return render_template(
        'index.html',
        title='WELCOME',
        curriculo=c
        )


if __name__ == '__main__':
    app.run(debug=True)

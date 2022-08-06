from flask import Flask, render_template
from utils.database import Curriculo

app = Flask(__name__)

c = Curriculo(
    id=1,
    url_img='foto.png',
    nome='Jucian Kauê Decezare',
    CPF='032.654.765-23',
    telefone='49989140512',
    email='juciandecezare@hotmail.com',
    resumo='Hello, my name is Jucian',
    ultimaatualizacao='Today',
    formacao=None,
    atuacao=None,
    projetos=None)

@app.route('/')
def main():
    return render_template(
        'index.html',
        title='WELCOME',
        curriculo=c
        )


if __name__ == '__main__':
    app.run(debug=True)

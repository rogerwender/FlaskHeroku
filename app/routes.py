from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Rogerio"
    dados = {"profissao": "Analista de Dados", "canal": "MeuCanal"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/custoplanosaude')
def custoplanosaude():
    return render_template('custoplanosaude.html')




from curso_flask import app, db
from flask import render_template as render, url_for, request
from curso_flask.models import Contato

@app.route('/')
def index():
    usuario = "Fábio"
    idade = 44

    context = {
        'usuario': usuario,
        'idade': idade
    }

    return render('index.html', context=context)


@app.route('/contato/', methods=['GET', 'POST'])
def novapagina():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({
            'pesquisa': pesquisa
        })
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            nome=nome, 
            email=email, 
            assunto=assunto, 
            mensagem=mensagem
        )
        db.session.add(contato)
        db.session.commit()

    return render('contato.html')
from curso_flask import app
from flask import render_template as render, url_for
    

@app.route('/')
def index():
    usuario = "Fábio"
    idade = 44

    context = {
        'usuario': usuario,
        'idade': idade
    }

    return render('index.html', context=context)


@app.route('/nova/')
def novapagina():
    return 'outra view'
from curso_flask import app
from flask import render_template as render


@app.route('/')
def index():
    return render('index.html')
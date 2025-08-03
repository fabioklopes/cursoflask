from flask import Flask

app = Flask(__name__)

# importação das rotas
from curso_flask.views import *
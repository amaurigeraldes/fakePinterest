# Arquivo __ini__ é obrigatório em uma aplicação Flask e é onde é definido o app
# Obs.: É onde é criado o nosso site

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
# Tratamento para situações do Banco de Dados ONLINE ou OFFLINE
# if os.getenv("DEBUG") == 0:
#     link_banco_dados = os.getenv("DATABASE_URL")
# else:
#     link_banco_dados = "sqlite:///comunidade.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "cee335885f8d3032694af2e5ba47fda0"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


# ------------------- IMPORTANTE --------------------
# ===================================================
# Esta importação precisa ser feita posterior ao app
# Obs.: Caso contrário gerará uma Referência Circular
from fakePinterest import routes
# ===================================================

# ------ ROTEIRO PARA CRIACÃO DE UMA APLICACÃO UTILIZANDO O FRAMEWORK FLASK ---------------
# *****************************************************************************************
# Estrutura básica obrigatória para funcionamento de uma aplicação Flask
# *****************************************************************************************
# Criação e ativação de um Ambiente Virtual para o Projeto: python -m venv PROJFAKEPNTEREST
# pip install flask
# pip install flask-login flask-bcrypt
# Criar o arquivo main.py para executar o projeto
# Criação de uma pasta do Projeto (exemplo: fakePinterest) que deverá conter:
# 1) Criar a pasta "templates" para organizar as imagens, etc
# 2) Criar o arquivo __init__.py para definição e criação do site
# 3) Criar o arquivo forms.py para criação dos formulários do site
# 4) Criar o arquivo models.py para criação da estrutura de banco de dados do site
# 5) Criar o arquivo routes.py para criação das rotas (links) do site
# *****************************************************************************************

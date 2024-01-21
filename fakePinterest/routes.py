# Criar as Rotas do nosso site (links) e criar a lógica de login

from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from fakePinterest import app, database, bcrypt
from fakePinterest.forms import FormLogin, FormCriarConta, FormFoto
from fakePinterest.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename


# Tela de login na conta
@app.route("/", methods = ["GET", "POST"])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email = form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha.encode("utf-8"), form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario = usuario.id))
    return render_template("homepage.html", form = form_login)



# Tela de criar conta
@app.route("/criarconta", methods = ["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data).decode("utf-8")
        usuario = Usuario(username = form_criarconta.username.data, 
                          senha = senha, 
                          email = form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember = True)
        return redirect(url_for("perfil", id_usuario = usuario.id))
    return render_template("criarconta.html", form = form_criarconta)



# Somente usuários logados poderão ter acesso ao perfil
@app.route("/perfil/<id_usuario>", methods = ["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        # O usuário está visualizando o perfil dele
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # Salvar o arquivo nome_seguro na Pasta fotos_posts
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config["UPLOAD_FOLDER"],
                                   nome_seguro)
            arquivo.save(caminho)
            # Registrar o arquivo nome_seguro no Banco de Dados
            foto = Foto(imagem = nome_seguro, id_usuario = current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template("perfil.html", usuario = current_user, form = form_foto)
    else:
        # O usuário está visualizando o perfil de outro usuário (poderá somente visualizar)
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario = usuario, form = None)



# Tela de logout da conta
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))



# Tela do Feed
@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    return render_template("feed.html", fotos = fotos)


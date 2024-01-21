# Criar os Formulários do nosso site

# pip install flask-wtf
# pip install email_validator

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakePinterest.models import Usuario


# Formulário para fazer Login
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators = [DataRequired(), Email()])
    senha = PasswordField("Senha", validators = [DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if not usuario:
            raise ValidationError("Usuário não cadastrado! Favor criar uma conta")


# Formulário para criar conta
class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators = [DataRequired(), Email()])
    username = StringField("Nome de usuário", validators = [DataRequired()])
    senha = PasswordField("Senha", validators = [DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de senha", validators = [DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar conta")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado! Faça o login para acessar a sua conta")    
        


# Formulário para Upload de Fotos
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators = [DataRequired()])
    botao_confirmacao = SubmitField("Enviar")

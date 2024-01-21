# Criando um Banco de Dados para o Projeto
# Obs.: Será criada uma Nova Pasta "var\fakePinterest-instance"
# Obs.2: Após a criação este Script não terá mais nenhuma função

from fakePinterest import database, app
from fakePinterest.models import Usuario, Foto


with app.app_context():
    database.create_all()
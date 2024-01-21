# Criando uma Secret Key

import secrets

# Gerar uma senha única com 16 dígitos para utilizar no __init__.py
print(secrets.token_hex(16))

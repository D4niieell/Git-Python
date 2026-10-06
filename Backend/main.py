import os
from dotenv import load_dotenv

load_dotenv
senha_correta = os.getenv("SENHA")

senha_digitada = input("Digite a senha: ")

if senha_digitada == senha_correta:
    print("Acesso autorizado")
else:
    print("Acesso negado")

# senha = "#senha.321"
import mysql.connector
from config import *

def conectar_db():
    conexao = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    # Alterar a linha abaixo
    cursor = conexao.cursor(dictionary=True)
    return conexao, cursor


def encerrar_db(cursor, conexao):
    cursor.close()
    conexao.close()
    
def limpar_input(campo):
    campolimpo = campo.replace(".","").replace("/","").replace("-","").replace(" ","").replace("(","").replace(")","").replace("R$","")
    return campolimpo
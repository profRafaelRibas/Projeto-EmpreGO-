ambiente = 'desenvolvimento'

if ambiente == 'desenvolvimento':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'suasenha'
    DB_NAME = 'suabasededados'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'emprego'

#ACESSO DO ADMIN
MASTER_EMAIL = 'adm@adm'
MASTER_PASSWORD = 'adm'
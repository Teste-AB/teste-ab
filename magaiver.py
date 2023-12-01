import mysql.connector
import string
import random

# Configuração do banco de dados
config = {
    'user': 'root',
    'password': 'fatec',
    'host': 'localhost',
    'database': 'metrica_AB',
    'raise_on_warnings': True
}

def connect():
    try:
        connection = mysql.connector.connect(**config)
        print("Conexão estabelecida com sucesso!")
        return connection
    except mysql.connector.Error as err:
        print(f'Erro: {err}')
        return None

def criar_tabela():
    connection = connect()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    email VARCHAR(255) PRIMARY KEY NOT NULL,
                    colocou_email BOOLEAN DEFAULT 0,
                    comprou BOOLEAN DEFAULT 0,
                    teste CHAR(1)
                );
            ''')
            print('Tabela criada com sucesso!')
        except mysql.connector.Error as err:
            print(f'Erro ao criar tabela: {err}')
        finally:
            connection.commit()
            connection.close()

def validar_dados(email):
    return email.strip() and ' ' not in email.strip()

def criar_usuario():
    try:
        email = input("Digite seu email:")
        teste = input("Qual teste o usuario ira receber? (A/B)")

        if not validar_dados(email):
            print('Erro: digite um email válido!')
            return

        connection = connect()
        if connection is not None:
            cursor = connection.cursor()
            try:
                cursor.execute('INSERT INTO usuario (email, colocou_email, comprou, teste) VALUES (%s, %s, %s, %s)', (email, False, False, teste))
                connection.commit()
                print('USUÁRIO CRIADO COM SUCESSO')
            except mysql.connector.Error as err:
                print(f'Erro ao inserir usuário: {err}')
            finally:
                connection.close()
    except Exception as e:
        print(f'Erro: {e}')

def listar_usuarios():
    connection = connect()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute('''SELECT email FROM usuario''')
            usuarios = cursor.fetchall()
            print('Lista de usuários:')
            for usuario in usuarios:
                print(usuario[0])
        except mysql.connector.Error as err:
            print(f'Erro ao listar usuários: {err}')
        finally:
            connection.close()

# Criar a tabela (se não existir)
criar_tabela()

# Opção do usuário
opcao = input('Deseja adicionar um novo email? (sim/não) ')

if opcao.lower() == 'sim':
    criar_usuario()
else:
    listar_usuarios()


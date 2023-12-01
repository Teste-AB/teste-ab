from flask import Flask, request, render_template, abort, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'user': 'root',
    'password': 'fatec',
    'host': 'localhost',
    'database': 'metrica_AB',
    'raise_on_warnings': True
}

# Conectar ao banco de dados
db_conn = mysql.connector.connect(**db_config)
cursor = db_conn.cursor()

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para registrar o clique na primeira tela
@app.route('/registrar_clique', methods=['POST'])
def registrar_clique():
    email = request.form.get('email')

    # Verificar se o e-mail está cadastrado
    check_email_query = "SELECT email, teste FROM usuario WHERE email = %s"
    cursor.execute(check_email_query, (email,))
    user_data = cursor.fetchone()

    if not user_data:
        abort(404)  # Retornar um erro 404 se o e-mail não estiver cadastrado

    email, teste = user_data

    # Atualizar a coluna 'colocou_email' para 1
    update_query = "UPDATE usuario SET colocou_email = 1 WHERE email = %s"
    cursor.execute(update_query, (email,))
    db_conn.commit()

    # Redirecionar com base no valor do campo 'teste'
    if teste == 'A':
        return redirect(url_for('pagina_a', email=email))
    elif teste == 'B':
        return redirect(url_for('pagina_b', email=email))
    else:
        abort(404)  # Redirecionar para página de erro se o valor de 'teste' não for 'A' nem 'B'


def verificar_tipo_usuario(email, tipo_esperado):
    # Consultar o tipo do usuário no banco de dados
    check_tipo_query = "SELECT teste FROM usuario WHERE email = %s"
    cursor.execute(check_tipo_query, (email,))
    tipo_usuario = cursor.fetchone()

    # Verificar se o tipo do usuário corresponde ao esperado
    return tipo_usuario and tipo_usuario[0] == tipo_esperado

# Rota para a página A
@app.route('/pagina_a/<email>')
def pagina_a(email):
    # Verificar se o tipo do usuário é 'A'
    if not verificar_tipo_usuario(email, 'A'):
        abort(403)  # Retornar erro 403 (proibido) se o usuário não tiver permissão
    return render_template('anuncioA.html', email=email)

# Rota para a página B
@app.route('/pagina_b/<email>')
def pagina_b(email):
    # Verificar se o tipo do usuário é 'B'
    if not verificar_tipo_usuario(email, 'B'):
        abort(403)  # Retornar erro 403 (proibido) se o usuário não tiver permissão
    return render_template('anuncioB.html', email=email)

# Rota para registrar a compra
@app.route('/registrar_compra', methods=['POST'])
def registrar_compra():
    email = request.form.get('email')

    # Atualizar a coluna 'comprou' para 1
    update_query = "UPDATE usuario SET comprou = 1 WHERE email = %s"
    cursor.execute(update_query, (email,))
    db_conn.commit()

    return render_template('compraFinalizada.html')

if __name__ == '__main__':
    app.run(debug=True)

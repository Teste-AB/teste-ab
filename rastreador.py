from flask import Flask, request, render_template, abort
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'user':'root',
    'password':'root',
    'host':'localhost',
    'database':'metrica_AB',
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
    check_email_query = "SELECT email FROM usuario WHERE email = %s"
    cursor.execute(check_email_query, (email,))
    existing_email = cursor.fetchone()

    if not existing_email:
        abort(404)  # Retornar um erro 404 se o e-mail não estiver cadastrado


    # Atualizar a coluna 'colocou_email' para 1
    update_query = "UPDATE usuario SET colocou_email = 1 WHERE email = %s"
    cursor.execute(update_query, (email,))
    db_conn.commit()

    return render_template('anuncio.html', email=email)

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

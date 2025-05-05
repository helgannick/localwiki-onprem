from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configuração de conexão com MySQL
import os

db = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'db'),  # nome do serviço no docker-compose
    user=os.getenv('DB_USER', 'user'),
    password=os.getenv('DB_PASSWORD', 'password'),
    database=os.getenv('DB_NAME', 'localwiki')
)

cursor = db.cursor()

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Artigos públicos
@app.route('/artigos')
def artigos():
    cursor.execute("SELECT id, titulo, conteudo, autor, data FROM artigos ORDER BY data DESC")
    dados = cursor.fetchall()
    artigos = [
        {
            'id': row[0],
            'titulo': row[1],
            'conteudo': row[2],
            'autor': row[3],
            'data': row[4].strftime('%d/%m/%Y')
        } for row in dados
    ]
    return render_template('artigos.html', artigos=artigos)

# Dashboard (admin)
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        autor = request.form['autor']
        data = datetime.now()

        cursor.execute(
            "INSERT INTO artigos (titulo, conteudo, autor, data) VALUES (%s, %s, %s, %s)",
            (titulo, conteudo, autor, data)
        )
        db.commit()
        return redirect(url_for('dashboard'))

    cursor.execute("SELECT id, titulo, autor, data FROM artigos ORDER BY data DESC")
    artigos = cursor.fetchall()
    return render_template('dashboard.html', artigos=artigos)

# Rodar servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

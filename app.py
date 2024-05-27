import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para adicionar receita ao banco de dados SQLite
def adicionar_receita(data, descricao, valor):
    try:
        conn = sqlite3.connect("financas.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO receitas (data, descricao, valor) VALUES (?, ?, ?)", (data, descricao, valor))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao adicionar receita: {e}")
        return False


def adicionar_despesa(data, descricao, valor):
    try:
        conn = sqlite3.connect("financas.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO despesas (data, descricao, valor) VALUES (?, ?, ?)", (data, descricao, valor))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao adicionar despesa: {e}")
        return False

# Função para gerar relatório (substitua esta lógica pela lógica de geração real)
def gerar_relatorio():
    # Aqui você pode implementar a lógica real para gerar um relatório
    # Substitua esta lógica pela sua implementação

    return True  # Retorno de sucesso fictício

# Rota para adicionar receita
@app.route('/add_receita', methods=['POST'])
def add_receita_route():
    data = request.form['data']
    descricao = request.form['descricao']
    valor = float(request.form['valor'])
    
    if adicionar_receita(data, descricao, valor):
        return jsonify({'status': 'adicionar com sucesso'})
    else:
        return jsonify({'status': 'erro ao adicionar'})

# Rota para adicionar despesa
@app.route('/add_despesa', methods=['POST'])
def add_despesa_route():
    data = request.form['data']
    descricao = request.form['descricao']
    valor = float(request.form['valor'])
    
    if adicionar_despesa(data, descricao, valor):
        return jsonify({'status': 'adicionar com sucesso'})
    else:
        return jsonify({'status': 'erro ao adicionar'})

# Rota para gerar relatório
@app.route('/gerar_relatorio', methods=['GET'])
def gerar_relatorio_route():
    if gerar_relatorio():
        return jsonify({'status': 'gerar relatório com sucesso'})
    else:
        return jsonify({'status': 'erro ao gerar relatório'})

if __name__ == '__main__':
    app.run(debug=True)
    
import psycopg2

# Conectar ao banco de dados
conn = psycopg2.connect(
    dbname="financeiro_db",
    user="seu_usuario",
    password="sua_senha",
    host="localhost"
)

# Criar um cursor para executar consultas SQL
cur = conn.cursor()

# Executar uma consulta SQL para selecionar todas as despesas
cur.execute("SELECT * FROM expenses")

# Obter os resultados da consulta
rows = cur.fetchall()

# Imprimir os resultados
for row in rows:
    print(row)

# Fechar o cursor e a conexão
cur.close()
conn.close()

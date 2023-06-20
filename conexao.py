import mysql.connector

def conectar_banco_dados():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="130993",
            database="controle_roupas"
        )
        print("Conexão com o banco de dados estabelecida.")
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None

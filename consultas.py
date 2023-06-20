def consulta_contagem_roupas_por_cor(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT Cor, COUNT(*) AS Quantidade FROM PecaRoupa GROUP BY Cor")
        resultado = cur.fetchall()
        print("Contagem de roupas por cor:")
        for row in resultado:
            print(f"Cor: {row[0]}, Quantidade: {row[1]}")
    except mysql.connector.Error as e:
        print(f"Erro ao executar consulta: {e}")

def consulta_media_tamanho_por_marca(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT Marca, AVG(Tamanho) AS Media FROM PecaRoupa GROUP BY Marca")
        resultado = cur.fetchall()
        print("Média de tamanho por marca:")
        for row in resultado:
            print(f"Marca: {row[0]}, Média: {row[1]}")
    except mysql.connector.Error as e:
        print(f"Erro ao executar consulta: {e}")


def consulta_join_peca_marca(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT PR.Nome AS NomePeca, MR.Nome AS NomeMarca, PR.Tamanho, PR.Cor, PR.Estacao "
                    "FROM PecaRoupa PR "
                    "LEFT JOIN MarcaRoupa MR ON PR.Marca = MR.Nome "
                    "LIMIT 0, 1000")
        resultado = cur.fetchall()
        print("Join detalahamento entre peças de roupa e marcas:")
        for row in resultado:
            nome_peca = row[0]
            nome_marca = row[1]
            tamanho = row[2]
            cor = row[3]
            estacao = row[4]
            print(f"Peça de Roupa: {nome_peca}, Marca: {nome_marca}, Tamanho: {tamanho}, Cor: {cor}, Estação: {estacao}")
    except mysql.connector.Error as e:
        print(f"Erro ao executar consulta: {e}")

def consulta_total_pecas(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM PecaRoupa")
        resultado = cur.fetchall()
        print("Dados da tabela PecaRoupa:")
        for row in resultado:
            print(row)
    except mysql.connector.Error as e:
        print(f"Erro ao executar consulta: {e}")

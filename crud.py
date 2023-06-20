def inserir_peca_roupa(conn, nome, tamanho, cor, marca, estacao, categoria, tecido):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO PecaRoupa (Nome, Tamanho, Cor, Marca, Estacao, Categoria, Tecido) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (nome, tamanho, cor, marca, estacao, categoria, tecido)
        cursor.execute(query, values)
        conn.commit()
        print("Peça de roupa inserida com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao inserir peça de roupa: {e}")

def atualizar_peca_roupa(conn, id_peca, novo_nome):
    try:
        cursor = conn.cursor()
        query = "UPDATE PecaRoupa SET Nome = %s WHERE ID = %s"
        values = (novo_nome, id_peca)
        cursor.execute(query, values)
        conn.commit()
        print("Peça de roupa atualizada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao atualizar peça de roupa: {e}")

def excluir_peca_roupa(conn, id_peca):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM PecaRoupa WHERE ID = %s"
        value = (id_peca,)
        cursor.execute(query, value)
        conn.commit()
        print("Peça de roupa excluída com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao excluir peça de roupa: {e}")

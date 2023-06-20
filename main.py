# Importação dos módulos necessários
from conexao import conectar_banco_dados
from crud import inserir_peca_roupa, atualizar_peca_roupa, excluir_peca_roupa
from consultas import consulta_contagem_roupas_por_cor, consulta_media_tamanho_por_marca, consulta_join_peca_marca, consulta_total_pecas

# Função que exibe e gerencia o menu principal
def menu_principal(conn):
    while True:
        # Exibição das opções do menu principal
        print("------- MENU PRINCIPAL -------")
        print("1. Inserir peça de roupa")
        print("2. Atualizar peça de roupa")
        print("3. Excluir peça de roupa")
        print("0. Consultas")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Solicita os dados da peça de roupa e chama a função de inserção
            nome = input("Nome da peça de roupa: ")
            tamanho = input("Tamanho: ")
            cor = input("Cor: ")
            marca = input("Marca: ")
            estacao = input("Estação: ")
            categoria = input("Categoria: ")
            tecido = input("Tecido: ")
            inserir_peca_roupa(conn, nome, tamanho, cor, marca, estacao, categoria, tecido)
        elif opcao == "2":
            # Solicita o ID da peça de roupa e o novo nome, e chama a função de atualização
            id_peca = input("ID da peça de roupa: ")
            novo_nome = input("Novo nome: ")
            atualizar_peca_roupa(conn, id_peca, novo_nome)
        elif opcao == "3":
            # Solicita o ID da peça de roupa e chama a função de exclusão
            id_peca = input("ID da peça de roupa: ")
            excluir_peca_roupa(conn, id_peca)
        elif opcao == "0":
            menu_consultas(conn)  # Chama o menu de consultas
        else:
            print("Opção inválida. Tente novamente.")

# Função que exibe e gerencia o menu de consultas
def menu_consultas(conn):
    while True:
        # Exibição das opções do menu de consultas
        print("------- MENU CONSULTAS -------")
        print("1. Contagem de roupas por cor")
        print("2. Média de tamanho por marca")
        print("3. Join detalhado entre peças de roupa e marcas")
        print("4. Consulta total de peças")
        print("0. Voltar para o menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consulta_contagem_roupas_por_cor(conn)  # Chama a consulta de contagem de roupas por cor
        elif opcao == "2":
            consulta_media_tamanho_por_marca(conn)  # Chama a consulta de média de tamanho por marca
        elif opcao == "3":
            consulta_join_peca_marca(conn)  # Chama a consulta de join entre peças de roupa e marcas
        elif opcao == "4":
            consulta_total_pecas(conn)  # Chama a consulta de consulta total de peças
        elif opcao == "0":
            break  # Encerra o loop e retorna ao menu principal
        else:
            print("Opção inválida. Tente novamente.")

# Estabelece a conexão com o banco de dados
conn = conectar_banco_dados()

# Verifica se a conexão foi estabelecida com sucesso
if conn is not None:
    menu_principal(conn)  # Chama o menu principal
    menu_consultas(conn)  # Chama o menu de consultas

# Relatório Trabalho Final - BDI
Universidade Federal de Santa Catarina

Centro Tecnológico - CTC

Departamento de Informática e Estatística

INE5613-04238B - Bancos de Dados I

Letícia S. Minosso - 20102275

# Relatório detalhamento do projeto

## **Descrição do objetivo geral do sistema**

O objetivo geral do sistema é fornecer um controle eficiente das peças de roupa em um armário, permitindo ao usuário gerenciar suas roupas com base em critérios como tamanho, cor, marca, estação, categoria e tecido. O sistema facilitará a busca por peças específicas, fornecerá informações detalhadas sobre cada item e permitirá a realização de consultas personalizadas para auxiliar na seleção e organização das roupas.

## **Descrição detalhada do sistema**

O sistema de controle de peças de roupa foi desenvolvido com o objetivo de oferecer aos usuários uma solução eficiente para gerenciar e organizar suas roupas. Com base em um banco de dados relacional, o sistema utiliza tabelas relacionadas para armazenar e manipular as informações das peças e marcas, permitindo um controle detalhado das roupas.

O banco de dados é composto por duas principais tabelas: "PecaRoupa" e "MarcaRoupa". A tabela "PecaRoupa" contém atributos como um identificador único (ID) para cada peça, nome da peça, tamanho, cor, estação, categoria e tecido. Já a tabela "MarcaRoupa" registra as informações das marcas, incluindo um identificador único (ID) e o nome da marca. A relação entre as tabelas é estabelecida por meio da coluna "MarcaID" na tabela "PecaRoupa", que associa cada peça à marca correspondente.

O sistema oferece diversas funcionalidades que facilitam o gerenciamento das peças de roupa. Uma das principais funcionalidades é o cadastro de novas peças, onde o usuário pode inserir informações detalhadas, como o nome da peça, tamanho, cor, marca, estação, categoria e tecido. Cada peça é identificada por um ID único, garantindo a integridade dos dados.

Além do cadastro, o sistema permite a atualização das informações das peças de roupa existentes. Por exemplo, o usuário pode alterar o tamanho de uma peça, modificar a cor, atualizar a marca associada, entre outras informações relevantes. Essa flexibilidade proporciona um controle preciso e atualizado das peças de roupa no armário.

Outra funcionalidade importante é a exclusão de peças de roupa. Caso o usuário não deseje mais manter uma determinada peça no armário, ele pode removê-la do sistema, garantindo uma organização eficiente das roupas disponíveis.

A consulta de peças de roupa é uma funcionalidade essencial para explorar as informações armazenadas no sistema. O usuário pode realizar consultas baseadas em diferentes critérios, como tamanho, cor, marca, estação, categoria e tecido. Por exemplo, é possível buscar todas as peças de roupa de determinada cor, visualizar as peças disponíveis em um determinado tamanho, ou filtrar as peças por estação. Essas consultas fornecem uma visão abrangente das roupas disponíveis, auxiliando na escolha do vestuário adequado para cada ocasião.

O sistema é projetado para proporcionar uma experiência intuitiva e amigável aos usuários. Através de uma interface simples e interativa, eles podem acessar as funcionalidades disponíveis, realizar as operações desejadas e obter informações relevantes sobre as peças de roupa cadastradas. O objetivo é facilitar o processo de organização do armário e garantir que as roupas sejam selecionadas de forma prática e eficiente.

Com o sistema de controle de peças de roupa, os usuários podem desfrutar de um armário bem organizado, tendo todas as informações necessárias sobre suas roupas ao alcance das mãos. Através do cadastro, atualização, exclusão e consulta de peças, eles podem manter um controle preciso e personalizado de seu vestuário, otimizando seu tempo e facilitando a seleção das roupas mais adequadas para cada ocasião.

## **Modelagem conceitual do projeto**

Entidades:

**PecaRoupa:**
ID (chave primária)
Nome
Tamanho
Cor
Estação
Categoria
Tecido
MarcaID (chave estrangeira referenciando a tabela MarcaRoupa)

**MarcaRoupa:**
ID (chave primária)
Nome

Relacionamento: PecaRoupa possui uma relação muitos-para-um com MarcaRoupa, indicado pela coluna MarcaID na tabela PecaRoupa, que referencia a tabela MarcaRoupa.

A modelagem conceitual representa as entidades envolvidas no sistema e os relacionamentos entre elas. A entidade PecaRoupa armazena informações específicas de cada peça, como seu identificador único (ID), nome, tamanho, cor, estação, categoria e tecido. A entidade MarcaRoupa registra as informações das marcas, contendo um identificador único (ID) e o nome da marca.

O relacionamento entre as entidades é estabelecido pela coluna MarcaID na tabela PecaRoupa, que referencia a tabela MarcaRoupa. Essa relação indica que uma peça de roupa está associada a uma marca específica. Dessa forma, é possível identificar a qual marca uma determinada peça pertence.

## **Modelagem Lógica**

A modelagem lógica é uma representação detalhada da estrutura do banco de dados, incluindo tabelas, colunas, tipos de dados e restrições. A partir da modelagem conceitual, é possível realizar a tradução para a modelagem lógica, definindo de forma precisa como os dados serão armazenados.

Para o projeto de controle de peças de roupa, a modelagem lógica considera as duas entidades principais: PecaRoupa e MarcaRoupa.

**Tabela PecaRoupa:**

ID: Identificador único da peça de roupa (chave primária)
Nome: Nome da peça de roupa (texto)
Tamanho: Tamanho da peça de roupa (texto)
Cor: Cor da peça de roupa (texto)
Estação: Estação em que a peça de roupa é adequada (texto)
Categoria: Categoria da peça de roupa (texto)
Tecido: Tecido da peça de roupa (texto)
MarcaID: Chave estrangeira que referencia o ID da tabela MarcaRoupa

**Tabela MarcaRoupa:**
ID: Identificador único da marca de roupa (chave primária)
Nome: Nome da marca de roupa (texto)

No modelo lógico, cada entidade é representada por uma tabela, onde cada coluna corresponde a um atributo da entidade. Na tabela PecaRoupa, por exemplo, temos as colunas ID, Nome, Tamanho, Cor, Estação, Categoria, Tecido e MarcaID. A coluna ID é a chave primária, garantindo a unicidade dos registros. A coluna MarcaID é uma chave estrangeira, referenciando o ID da tabela MarcaRoupa e estabelecendo uma relação entre as duas entidades.

A tabela MarcaRoupa, por sua vez, possui as colunas ID e Nome. O ID é a chave primária, garantindo a unicidade dos registros, enquanto a coluna Nome armazena o nome da marca de roupa.

Com a modelagem lógica, podemos visualizar de forma clara a estrutura do banco de dados e as relações entre as entidades. Essa representação é essencial para a criação das tabelas no banco de dados e para a implementação do sistema de controle de peças de roupa.

## **Script DDL**

```sql
--- Criação da tabela MarcaRoupa

CREATE TABLE MarcaRoupa (
ID INT PRIMARY KEY,
Nome VARCHAR(100)
);

--- Criação da tabela PecaRoupa:

CREATE TABLE PecaRoupa (
ID INT PRIMARY KEY,
Nome VARCHAR(100),
Tamanho VARCHAR(20),
Cor VARCHAR(50),
Estacao VARCHAR(50),
Categoria VARCHAR(50),
Tecido VARCHAR(50),
MarcaID INT,
FOREIGN KEY (MarcaID) REFERENCES MarcaRoupa(ID)
);
```

## **DML**

Inserção de registros na tabela MarcaRoupa

```sql
INSERT INTO MarcaRoupa (ID, Nome) VALUES
(1, 'Nike'),
(2, 'Adidas'),
(3, 'GAP'),
(4, 'Zara'),
(5, 'H&M'),
(6, 'Calvin Klein'),
(7, 'Tommy Hilfiger'),
(8, 'Levis'),
(9, 'Ralph Lauren'),
(10, 'Puma');
```

Inserção de registros na tabela PecaRoupa

```sql
INSERT INTO PecaRoupa (ID, Nome, Tamanho, Cor, Estacao, Categoria, Tecido, MarcaID) VALUE
(1, 'Camiseta Branca', 'M', 'Branco', 'Verão', 'Camiseta', 'Algodão', 1),
(2, 'Calça Jeans', '38', 'Azul', 'Inverno', 'Calça', 'Jeans', 4),
(3, 'Vestido Floral', 'P', 'Vermelho', 'Primavera', 'Vestido', 'Viscose', 5),
(4, 'Blusa de Tricô', 'G', 'Cinza', 'Outono', 'Blusa', 'Lã', 3),
(5, 'Shorts Jeans', '36', 'Azul', 'Verão', 'Shorts', 'Jeans', 2),
(6, 'Camisa Social', 'M', 'Branco', 'Qualquer', 'Camisa', 'Algodão', 6),
(7, 'Jaqueta de Couro', 'G', 'Preto', 'Inverno', 'Jaqueta', 'Couro', 9),
(8, 'Saia Plissada', 'P', 'Rosa', 'Primavera', 'Saia', 'Poliéster', 7),
(9, 'Moletom Cinza', 'G', 'Cinza', 'Outono', 'Moletom', 'Algodão', 4),
(10, 'Bermuda Esportiva', 'M', 'Preto', 'Verão', 'Bermuda', 'Poliamida', 10);
```

### **Consultas**

Consulta de contagem de peças por marca

```sql
SELECT m.Nome AS Marca, COUNT(p.ID) AS Quantidade
FROM MarcaRoupa m
LEFT JOIN PecaRoupa p ON m.ID = p.MarcaID
GROUP BY m.Nome;
```

Consulta de média de tamanhos das peças por categoria:

```sql
SELECT pr.Categoria, AVG(pr.Tamanho) AS MediaTamanho
FROM PecaRoupa pr
GROUP BY pr.Categoria;
```

Consulta de todas as peças de roupa com informações de marca:

```sql
SELECT p.Nome AS Peca, p.Tamanho, p.Cor, p.Estacao, m.Nome AS Marca
FROM PecaRoupa p
LEFT JOIN MarcaRoupa m ON p.MarcaID = m.ID;
```

# Aplicação com conexão ao banco de dados

### Códigos do arquivo conexao.py

Para conectar com o banco usamos a função `conectar_banco_dados()`:

```python
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
```

Essa função estabelece uma conexão com o banco de dados MySQL. Ela utiliza a biblioteca `mysql.connector` para realizar a conexão. São fornecidos os seguintes parâmetros:

- `host`: O endereço do servidor do banco de dados. Nesse caso, está definido como "localhost", indicando que o banco de dados está sendo executado na mesma máquina.
- `user`: O nome de usuário usado para autenticar a conexão com o banco de dados. No exemplo, está definido como "root".
- `password`: A senha usada para autenticar a conexão com o banco de dados. No exemplo, está definida como "130993".
- `database`: O nome do banco de dados que se deseja conectar. No exemplo, está definido como "controle_roupas".

Se a conexão for estabelecida com sucesso, uma mensagem informando isso é exibida e o objeto de conexão `conn` é retornado. Caso ocorra algum erro durante a conexão, uma mensagem de erro é exibida e a função retorna `None`.

### Códigos do arquivo crud.py

```python
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

```

Essa função insere uma nova peça de roupa na tabela `PecaRoupa`. Ela recebe os parâmetros necessários para preencher as colunas da tabela e executa uma instrução SQL de inserção. Os valores são passados para a consulta usando o método `execute()` do cursor. Após a execução bem-sucedida, a transação é confirmada com `conn.commit()` e uma mensagem de sucesso é exibida.

```python
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

```

Essa função atualiza o nome de uma peça de roupa na tabela `PecaRoupa`. Ela recebe o ID da peça a ser atualizada e o novo nome. A instrução SQL de atualização é executada, substituindo o nome antigo pelo novo valor. Após a execução bem-sucedida, a transação é confirmada com `conn.commit()` e uma mensagem de sucesso é exibida.

```python
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

```

Essa função exclui uma peça de roupa da tabela `PecaRoupa` com base no seu ID. A instrução SQL de exclusão é executada, utilizando o ID fornecido como filtro. Após a execução bem-sucedida, a transação é confirmada com `conn.commit()` e uma mensagem de sucesso é exibida.

### Códigos do arquivo main.py

```python
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
```

### Códigos do arquivo consultas.py

```python
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

```

Essa função realiza uma consulta no banco de dados para obter a contagem de roupas por cor. Ela utiliza a cláusula `GROUP BY` para agrupar as roupas por cor e a função de agregação `COUNT(*)` para contar a quantidade de roupas em cada grupo. Os resultados são impressos na tela, exibindo a cor e a quantidade de roupas correspondentes.

```python
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

```

Essa função realiza uma consulta no banco de dados para calcular a média de tamanho das roupas por marca. Ela utiliza a cláusula `GROUP BY` para agrupar as roupas por marca e a função de agregação `AVG(Tamanho)` para calcular a média dos tamanhos em cada grupo. Os resultados são impressos na tela, exibindo a marca e a média de tamanho correspondente.

```python
def consulta_join_peca_marca(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT PR.Nome AS NomePeca, MR.Nome AS NomeMarca, PR.Tamanho, PR.Cor, PR.Estacao "
                    "FROM PecaRoupa PR "
                    "LEFT JOIN MarcaRoupa MR ON PR.Marca = MR.Nome "
                    "LIMIT 0, 1000")
        resultado = cur.fetchall()
        print("Join detalhamento entre peças de roupa e marcas:")
        for row in resultado:
            nome_peca = row[0]
            nome_marca = row[1]
            tamanho = row[2]
            cor = row[3]
            estacao = row[4]
            print(f"Peça de Roupa: {nome_peca}, Marca: {nome_marca}, Tamanho: {tamanho}, Cor: {cor}, Estação: {estacao}")
    except mysql.connector.Error as e:
        print(f"Erro ao executar consulta: {e}")

```

Essa função realiza um join entre as tabelas `PecaRoupa` e `MarcaRoupa` para obter informações detalhadas sobre as peças de roupa e suas marcas correspondentes. Os resultados são impressos na tela, exibindo o nome da peça de roupa, o nome da marca, o tamanho, a cor e a estação de cada peça.

```python
def consulta_total_pecas(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM PecaRoupa")
        resultado

 = cur.fetchall()
        print("Dados da tabela PecaRoupa:")
        for row in resultado:
            print(row)
    except mysql.connector.Error as e:
        print(f"Erro ao executar consulta: {e}")

```

Essa função realiza uma consulta simples no banco de dados para obter todos os dados da tabela `PecaRoupa`. Os resultados são impressos na tela, exibindo todas as colunas e registros da tabela.

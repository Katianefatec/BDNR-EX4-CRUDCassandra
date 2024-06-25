from connect_database import db

def delete_usuario(nome, sobrenome):
    query = "DELETE FROM usuario WHERE nome = %s AND sobrenome = %s"
    db.session.execute(query, (nome, sobrenome))
    print("Deletado o usuário com nome:", nome, "e sobrenome:", sobrenome)

def input_with_cancel(prompt, cancel_keyword="CANCELAR", cancel_on_n_for_specific_prompt=False):
    resposta = input(f"{prompt} (digite {cancel_keyword} para abortar): ")
    if resposta.upper() == cancel_keyword:
        print("Operação cancelada.")
        return None
    if cancel_on_n_for_specific_prompt and resposta.upper() == 'N':
        return resposta
    return resposta

def create_usuario():
    print("\nInserindo um novo usuário")
    nome = input_with_cancel("Nome")
    if nome is None: return

    sobrenome = input_with_cancel("Sobrenome")
    if sobrenome is None: return
    
    cpf = input_with_cancel("CPF")
    if cpf is None or cpf.strip() == "":  
        print("CPF é obrigatório.")
        return

    # Verificar se já existe um usuário com o mesmo CPF
    query = "SELECT * FROM usuario WHERE cpf = %s"
    if db.session.execute(query, (cpf,)).one():
        print("Já existe um usuário cadastrado com este CPF.")
        return
    
    end = []
    # O Cassandra não suporta listas de mapas diretamente como o MongoDB, então isso precisa ser adaptado.
    # Pode-se serializar a lista de endereços em uma string JSON, por exemplo, ou modelar de outra forma.

    # Inserir usuário
    query = "INSERT INTO usuario (nome, sobrenome, cpf, end) VALUES (%s, %s, %s, %s)"
    db.session.execute(query, (nome, sobrenome, cpf, str(end)))  # end como string JSON, por exemplo
    print("Usuário inserido com sucesso.")

def read_usuario(nome):
    if not nome:
        query = "SELECT * FROM usuario"
        for row in db.session.execute(query):
            print(row.nome, row.cpf)
    else:
        query = "SELECT * FROM usuario WHERE nome = %s"
        for row in db.session.execute(query, (nome,)):
            print(row)

def update_usuario(nome):
    # Buscar usuário
    query = "SELECT * FROM usuario WHERE nome = %s"
    user = db.session.execute(query, (nome,)).one()
    if user:
        print("Dados do usuário: ", user)
        novo_nome = input("Mudar Nome:")
        sobrenome = input("Mudar Sobrenome:")
        cpf = input("Mudar CPF:")
        # Atualizar usuário
        query = "UPDATE usuario SET nome = %s, sobrenome = %s, cpf = %s WHERE nome = %s"
        db.session.execute(query, (novo_nome, sobrenome, cpf, nome))
        print("Usuário atualizado.")
    else:
        print("Usuário não encontrado.")
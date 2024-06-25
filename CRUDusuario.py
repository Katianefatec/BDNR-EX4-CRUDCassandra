from astrapy.collection import Collection
from connect_database import db

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

    collection: Collection = db.get_collection("usuario")  
    existing_user = collection.find_one({"cpf": cpf})  # Use find_one para buscar por CPF
    if existing_user:
        print("Já existe um usuário cadastrado com este CPF.")
        return

    end = []  

    # Inserir usuário (corrigido)
    collection.insert_one(document={"nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end})  
    print("Usuário inserido com sucesso.")
    


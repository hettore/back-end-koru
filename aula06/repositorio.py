from datetime import datetime
import sqlite3
import os

caminho = f"{os.path.dirname(__file__)}\\db\\harry_potter.db"

#Conectar com o banco de dados
# conexao = sqlite3.connect(caminho)

#Este script simula funcionalidades de banco de dados para o nosso projeto de CRUD

#O dicionario é nosso repositório principal EXEMPLO!!!
# personagens = {
#     1: {
#         "nome": "Harry Potter",
#         "raça": "Humano",
#         "casa": "Grifinória",
#         "altura": 1.80,
#         "nascimento": "31/07/1980",
#         "imagem": "https://upload.wikimedia.org/wikipedia/commons/9/97/Harry_Potter.jpg"
#     }

#tratamento de datas
def tratar_iso_para_dmy(data:str):
    if "-" in data:
        data = datetime.strptime(data, '%Y-%m-%d')
        return data.strftime('%d/%m/%Y')
    else:
        return data
    
def tratar_dmy_para_iso(data:str):
    if "/" in data:
        data = datetime.strptime(data, '%d/%m/%Y')
        return data.strftime('%Y/%m/%d')
    else:
        return data

#Função para gerar um novo id
def gerar_id():
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='personagens'")
    next_id = cursor.fetchone()[0]
    return next_id + 1

#Criar um novo personagem no dicionário
def criar_personagem(nome, raca, casa, nascimento, altura, imagem):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, nascimento_personagem, altura_personagem, imagem_personagem) values (?, ?, ?, ?, ?, ? )"
        cursor.execute(sql_insert, (nome, raca, casa, nascimento, altura, imagem))
        personagem_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return personagem_id
    except Exception as ex:
        print(ex)
        return 0

#Retorna um dicionário com todos os personagens
def retornar_personagens():
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_select = "SELECT * FROM personagens"
        cursor.execute(sql_select)
        personagens = cursor.fetchall()
        conn.close()
        return personagens
    except:
        return False    

#Retorna um único personagem
def retornar_personagem(id:int):
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", "", ""
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        sql_select = "SELECT * FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, raca, casa, nascimento, altura, imagem = cursor.fetchone()
        conn.close()
        return id, nome, raca, casa, nascimento, altura, imagem
    except:
        return False

#Atualiza os dados de um personagem
def atualizar_personagem(id:int, nome, raca, casa, nascimento, altura, imagem):
    try:
        #Tentar atualizar
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome_personagem = ?, raca_personagem = ?, casa_personagem = ?, nascimento_personagem = ?, altura_personagem = ?, imagem_personagem = ? WHERE id_personagem = ?"
        cursor.execute(sql_update, (nome, raca, casa, nascimento, altura, imagem, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    

#Remove um personagem
def remover_personagem(id:int):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()
        sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    

'''
nome = "Harry Potter"
raca = "Humano"
casa = "Grifinória"
altura = 1.80
nascimento = "31/07/1980"
imagem = "https://upload.wikimedia.org/wikipedia/commons/9/97/Harry_Potter.jpg"

id = criar_personagem(nome, raca, casa, altura, nascimento, imagem)
print(id)
print(retornar_personagem(id))

id, nome, raca, casa, altura, nascimento, imagem = retornar_personagem(id)
atualizar_personagem(id, "Harry James Potter", raca, casa, altura, nascimento, imagem)

print(retornar_personagem(id))
id, nome, raca, casa, altura, nascimento, imagem = retornar_personagem(id)

print(retornar_personagens())

remover_personagem(id)

print(retornar_personagens())
'''
import sqlite3
import os

caminho = f"{os.path.dirname(__file__)}\\bd\\harry_potter.db"

#Conectar com o banco de dados
conexao = sqlite3.connect(caminho)

#Criando os dados q vou manipular no banco
# nome = "Harry Potter"
# raca = "humano"
# casa = "Grifinória"
# altura = "1.80"
# nascimento = "31/07/1980"
# imagem = "https://upload.wikimedia.org/wikipedia/commons/9/97/Harry_Potter.jpg"

#Inserir dados no banco
# cursor = conexao.cursor()
# sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, altura_personagem, nascimento_personagem, imagem_personagem) VALUES (?, ?, ?, ?, ?, ?)"

# cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))

# personagem_id = cursor.lastrowid
# conexao.commit()
# print(f"O último código inserido foi: {personagem_id}")

# print("Personagem de código 2")
# cursor = conexao.cursor()
# sql_select_unico = "SELECT * FROM personagens WHERE id_personagem = ?"
# cursor.execute(sql_select_unico, (2, ))
# id, nome, raca, casa, nascimento, altura, imagem = cursor.fetchone()
# print(f"{id} ------ {nome}")

# sql_select_varios = "SELECT * FROM personagens"
# cursor.execute(sql_select_varios)
# lista_personagens =cursor.fetchall()
# for item in lista_personagens:
#     id, nome, raca, casa, nascimento, altura, imagem = item
#     print(f"{id} ---- {nome}")

# Atualizando um personagem
cursor = conexao.cursor()
sql_update = "UPDATE personagens SET nome_personagem = ? WHERE id_personagem = ?"
cursor.execute(sql_update, ("Harry James Potter", 1))


cursor = conexao.cursor()
sql_delete = "DELETE from personagens WHERE id_personagem = ?"
cursor.execute(sql_delete, (1, ))

sql_select_unico = "SELECT * FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_select_unico, (1, ))
print(cursor.fetchone())

from datetime import datetime
#Este script simula funcionalidades de banco de dados para o nosso projeto de CRUD

#O dicionario é nosso repositório principal
personagens = {
    1: {
        "nome": "Harry Potter",
        "raça": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/9/97/Harry_Potter.jpg"
    },
    2: {
        "nome": "Ron Weasley",
        "raça": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "01/03/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5e/Ron_Weasley_poster.jpg"
    },
    3: {
        "nome": "Hermione Granger",
        "raça": "Humano",
        "casa": "Grifinória",
        "altura": 1.65,
        "nascimento": "19/09/1979",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Hermione_Granger_by_Reilly_Brown.JPG"
    },
    4: {
        "nome": "Draco Malfoy",
        "raça": "Humano",
        "casa": "Sonserina",
        "altura": 1.80,
        "nascimento": "05/06/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Drago_Malefoy.jpg/320px-Drago_Malefoy.jpg"
    }
}

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
    id = len(personagens) + 1
    return id

#Criar um novo personagem no dicionário
def criar_personagem(nome, raca, casa, altura, nascimento, imagem):
    personagens[gerar_id()] = {"nome":nome, "raca":raca, "casa":casa, "altura":altura, "nascimento":nascimento, "imagem":imagem}

#Retorna um dicionário com todos os personagens
    # for id, personagem in personagens.items():
    #     personagem["nascimento"] = tratar_dmy_para_iso(personagem["nascimento"])
def retornar_personagens():

    return personagens

#Retorna um único personagem
        # personagens[id]["nascimento"] = tratar_dmy_para_iso(personagens[id]["nascimento"])
def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else: 
        return {}

#Atualiza os dados de um personagem
    # dados_personagem['nascimento'] = tratar_iso_para_dmy(dados_personagem['nascimento'])
def atualizar_personagem(id:int, dados_personagem:dict):

    personagens[id] = dados_personagem

#Remove um personagem
def remover_personagem(id):
    del personagens[id]

#Testes das funções
# print(retornar_personagens())

# criar_personagem("hettore", "Humano", "Grifinória", 1.73, "24/04/1991", "")

# print(retornar_personagem(5))

# atualizar_personagem(5, {'nome': 'hettore Eduardo', 'raca': 'Humano', 'casa': 'Grifinória', 'altura': 1.73, 'nascimento': '24/04/1991', 'imagem': ''})

# print(retornar_personagem(5))

# remover_personagem(5)

# print(retornar_personagem(5))
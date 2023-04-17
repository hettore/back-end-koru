from flask import Flask, render_template

dicionario = {
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
        "imagem": "https://upload.wikimedia.org/wikipedia/ed/d/d3/Hermione_Granger_poster.jpg"
    },
    4: {
        "nome": "Draco Malfoy",
        "raça": "Humano",
        "casa": "Sonserina",
        "altura": 1.80,
        "nascimento": "05/06/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Draco_Malfoy.jpg"
    }
}

def retorna_personagem(personagem):
    texto_retorno = f"<h1>{personagem['nome']}</h1><p>É {personagem['raça']} e sua casa é a {personagem['casa']}</p>"
    return texto_retorno

app = Flask(__name__)
@app.route("/")
def teste():
    return retorna_personagem(dicionario[1])

@app.route("/personagem/<int:personagem_id>")
def mostra_personagem(personagem_id):
    return render_template('/personagem.html', **dicionario[personagem_id])

app.run(debug=True)
# print(dicionario[1])
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

app = Flask(__name__)

@app.route("/personagem/<int:personagem_id>")
def mostra_personagem(personagem_id):
    return render_template('/personagem.html', **dicionario[personagem_id])

@app.route("/personagem_boot/<int:personagem_id>")
def mostra_personagem_boot(personagem_id):
    return render_template('/personagem_boot.html', **dicionario[personagem_id])

@app.route("/")
def mostra_personagens():
    return render_template('personagens.html', personagens=dicionario)

app.run(debug=True)

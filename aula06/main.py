from flask import Flask, render_template, request, redirect, url_for
import repositorio



app = Flask(__name__)

@app.route("/")
def home():
    lista_personagens = repositorio.retornar_personagens()
    return render_template("index.html", dados=lista_personagens)

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):

    if request.method == "POST":
        #Quer dizer que o usuário está mandando dados
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect(url_for('home'))
        elif "salvar" in request.form:
            id = request.form["id"]
            nome = request.form["nome"]
            raca = request.form["raca"]
            casa = request.form["casa"]
            altura = request.form["altura"]
            nascimento = request.form["nascimento"]
            imagem = request.form["imagem"]

            dados_retornados = repositorio.retornar_personagem(id)
            if dados_retornados:
                repositorio.atualizar_personagem(id=id, nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)
            else:
                repositorio.criar_personagem(nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)
            
            return redirect(url_for('home'))

    else:
        #retorna os dados de um personagem na página de cadastro
        id, nome, raca, casa, nascimento, altura, imagem = repositorio.retornar_personagem(id)
        
        return render_template("cadastro.html", id = id, nome = nome, casa = casa, raca = raca, nascimento = nascimento, altura = altura, imagem = imagem)
    


app.run(debug=True)

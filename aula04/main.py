from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

@app.route("/")
def home():
    dicionario = repositorio.retornar_personagens()
    return render_template("index.html", dados=dicionario)

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):

    if request.method == "POST":
        #Quer dizer que o usuário está mandando dados
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect(url_for('home'))
        elif "salvar" in request.form:
            personagem = {}
            personagem['nome'] = request.form['nome']
            personagem['casa'] = request.form['casa']
            personagem['raca'] = request.form['raca']
            personagem['altura'] = request.form['altura']
            personagem['nascimento'] = request.form['nascimento']
            personagem['imagem'] = request.form['imagem']

            if id in repositorio.retornar_personagens().keys():
                repositorio.atualizar_personagem(id, personagem)
            
            return redirect(url_for('home'))

    else:
        #retorna os dados de um personagem na página de cadastro
        personagem = repositorio.retornar_personagem(id)
        personagem['id'] = id
        return render_template("cadastro.html", **personagem)
    
@app.route("/personagem", methods=["GET", "POST"])
def criar_personagem():
    if request.method == "POST":
            personagem = {}
            personagem['nome'] = request.form['nome']
            personagem['casa'] = request.form['casa']
            personagem['raca'] = request.form['raca']
            personagem['altura'] = request.form['altura']
            personagem['nascimento'] = request.form['nascimento']
            personagem['imagem'] = request.form['imagem']
            repositorio.criar_personagem(**personagem)
            return redirect(url_for('home'))
    else:
        return render_template('cadastro.html', id=repositorio.gerar_id())

app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste")
def teste_rota():
    return "Esta é outra página<br><b>Funcionou!</b>"

app.run(debug=True)
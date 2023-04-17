# dicionario = {
#     "nome": "Hettore Eduardo",
#     "altura": 1.73,
#     "profissão": "Desenvolvedor Back-end e Aluno"
# }

# print(dicionario)

def retornar_produto(produto):
    texto_saida = f"Nome: {produto['nome']}\nDescrição: {produto['descricao']}\nPeso: {produto['peso']}\nValor: {produto['valor']}\nLançamento: {produto['lancamento']}"
    return texto_saida

produto_principal = {}

#iniciando a coleta de dados informados pe usuário
produto_principal["nome"] = input("Por favor, informe o nome do produto: ")
produto_principal["descricao"] = input("Por favor, informe a descrição do produto: ")
produto_principal["lancamento"] = int(input("Por favor, informe o ano de lançamento do produto: "))
produto_principal["valor"] = float(input("Por favor informe o valor do produto em reais: "))
produto_principal["peso"] = float(input("Por favor, informe o peso do produto em kg: "))

#print(produto)

# for chave, valor in produto.items():
#     print(f"{chave} - {valor}")

print(retornar_produto(produto_principal))
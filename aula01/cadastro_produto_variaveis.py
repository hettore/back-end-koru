def exibir_produto():
    print(f"Nome: {nome_produto}")
    print(f"Descrição: {descricao_produto}")
    print(f"Peso: {peso_produto}")
    print(f"Valor: {valor_produto}")
    print(f"Lançamento: {ano_lancamento_produto}")

def retornar_produto():
    texto_saida = f"Nome: {nome_produto}\n Descrição: {descricao_produto}\n Peso: {peso_produto}\n Valor: {valor_produto}\n Lançamento: {ano_lancamento_produto}"
    return texto_saida

print("Cadastro de produtos")

#iniciando a coleta de dados informados pe usuário
nome_produto = input("Por favor, informe o nome do produto: ")
descricao_produto = input("Por favor, informe a descrição do produto: ")
ano_lancamento_produto = int(input("Por favor, informe o ano de lançamento do produto: "))
valor_produto = float(input("Por favor informe o valor do protudo em reais: "))
peso_produto = float(input("Por favor, informe o peso do produto em kg: "))

#Exibição simples das variáveis
# print(nome_produto)
# print(descricao_produto)
# print(ano_lancamento_produto)
# print(valor_produto)
# print(peso_produto)

#Exibição de texto formatado
# print(f"Nome: {nome_produto}")
# print(f"Descrição: {descricao_produto}")
# print(f"Peso: {peso_produto}")
# print(f"Valor: {valor_produto}")
# print(f"Lançamento: {ano_lancamento_produto}")

print(retornar_produto())


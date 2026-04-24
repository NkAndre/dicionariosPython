import requests

# 1. Definição do link e requisição
link = "https://economia.awesomeapi.com.br/last/USD-BRL,ARS-BRL,ETH-BRL"
requisicao = requests.get(link)
dicMoedas = requisicao.json()

# 2. Menu de opções para o usuário
print("=== CONSULTA DE COTAÇÕES ===")
print("Escolha uma opção:")
print("1 - Dólar Americano")
print("2 - Peso Argentino")
print("3 - Ethereum")

opcao = input("Digite o número da moeda desejada: ")

# 3. Lógica de exibição baseada na escolha
if opcao == '1':
    nome = dicMoedas['USDBRL']['name']
    valor = dicMoedas['USDBRL']['bid']
    print(f"A cotação do {nome} é: R$ {valor}")

elif opcao == '2':
    nome = dicMoedas['ARSBRL']['name']
    valor = dicMoedas['ARSBRL']['bid']
    print(f"A cotação do {nome} é: R$ {valor}")

elif opcao == '3':
    nome = dicMoedas['ETHBRL']['name']
    valor = dicMoedas['ETHBRL']['bid']
    print(f"A cotação do {nome} é: R$ {valor}")

else:
    print("Opção inválida! Tente novamente.")
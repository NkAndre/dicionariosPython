import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,ARS-BRL,ETH-BRL"

# 2. requisao e transformacao
requisicao = requests.get(link)
dicMoedas = requisicao.json()


valor_dolar = dicMoedas['USDBRL']['bid']
valor_peso = dicMoedas['ARSBRL']['bid']
valor_ethereum = dicMoedas['ETHBRL']['bid']

# 4. exbicao do resultadp
print("=== COTAÇÕES DE HOJE ===")
print(f"Valor do Dólar americano hoje: R$ {valor_dolar}")
print(f"Valor do Peso argentino hoje: R$ {valor_peso}")
print(f"Valor do Ethereum hoje: R$ {valor_ethereum}")
import requests


link = "http://api.tempo.com/index.php?api_lang=br&localidad=12996&affiliate_id=tk99un15usak&v=3.0"
requisicao = requests.get(link)
dicRequisicao = requisicao.json()

# . Interface Interativa,p usuario escolher
print("=== PREVISÃO DO TEMPO INTERATIVA ===")
print("Escolha o dia que deseja consultar:")
print("1 - Hoje")
print("2 - Amanhã")
print("3 - Depois de amanhã")
print("4 - Daqui a 3 dias")

escolha = input("Digite o número (1-4): ")



if escolha in dicRequisicao.get("day", {}):
    previsao = dicRequisicao["day"][escolha]

    # Extração de dados, get é quando é pra evitar erro caso a key nao exista
    dia = previsao.get("date", "Desconhecido")
    diaSemana = previsao.get("name", "Desconhecido")
    descricaoTempo = previsao.get("symbol_description", "Sem descrição")
    tempMin = previsao.get("tempmin", "N/A")
    tempMax = previsao.get("tempmax", "N/A")
    vento = previsao.get("wind", {}).get("speed", "N/A")
    umidade = previsao.get("humidity", "N/A")
    dados_lua = previsao.get("moon", {})
    fasesLua = dados_lua.get("desc", dados_lua.get("symbol_description", "Dados não disponíveis"))

    # Exibição formatada naquele pique
    print("\n" + "="*30)
    print(f"RELATÓRIO PARA: {diaSemana} ({dia})")
    print("-" * 30)
    print(f"Clima: {descricaoTempo}")
    print(f"Temperatura: {tempMin}°C a {tempMax}°C")
    print(f"Vento: {vento} km/h")
    print(f"Umidade: {umidade}%")
    print(f"Fase da Lua: {fasesLua}")
    print("="*30)
else:
    print("\nOpção inválida ou dados não disponíveis para este dia.")
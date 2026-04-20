import requests
localidade = input('Digite o código da localidade (ex: 12996): ').strip()
affiliate_id = input('Digite o seu ID de afiliado: ').strip()

idioma = input("digite o idoma (ex:br) : ").strip()

versao = "3.0" ##deixei ele fixo a versao da APi
link = f"http://api.tempo.com/index.php?api_lang={idioma}&localidad={localidade}&affiliate_id={affiliate_id}&v={versao}"

requisicao = requests.get(link)
dicTempo = requisicao.json()
print(dicTempo)

print("-" * 30)
print("Link Gerado:")
print(link)
print("-" * 30)
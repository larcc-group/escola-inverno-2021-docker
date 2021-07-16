import sys
import matplotlib.pyplot as plt
import csv

dados = 'data/average-attendance-2003-2019.txt'
ano_legenda = '2003-2019'
ano = None
if len(sys.argv) > 1:
    ano = sys.argv[1]
    ano_legenda = ano

clubes = {}
with open(dados, newline='', encoding='iso-8859-1') as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')
    next(leitor) # pula a linha de cabeçalho
    for linha in leitor:
        nome_clube = linha[1]
        media_publico = int(linha[2])
        if ano != None and linha[0] != ano:
            # Se tiver filtro por ano, ignora dados de outros anos
            continue
        if not nome_clube in clubes:
            clubes[nome_clube] = 0
        clubes[nome_clube] = clubes[nome_clube]+media_publico

# Ordena os clubes por público, descrescente
clubes = dict(sorted(clubes.items(), key=lambda item: item[1], reverse=True))

# Conta quantos clubes temos
ticks = list(range(0, len(clubes)))

# Agora vamos gerar o gráfico
plt.title('Média de público nos estádios em ' + ano_legenda)
plt.bar(ticks, clubes.values())
plt.xticks(ticks, clubes.keys(), rotation='vertical')
plt.savefig('average-attendance-'+ano_legenda+'.png', dpi=150, bbox_inches='tight')

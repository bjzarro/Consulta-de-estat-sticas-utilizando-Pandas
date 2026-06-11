import pandas as pd
import random as r

df = pd.read_csv('tabela.csv', sep=';')
i = int(input("Digite de qual linha você quer as estatíticas: "))
linha = df.iloc[i-2] # Conta a linha do cabeçalho e o índice do pandas começa em 0

TimeCasa = linha["TimeCasa"]
TimeFora = linha["TimeFora"]
Chutes_Casa = linha["Chutes_Casa"]
Chutes_Fora = linha["Chutes_Fora"]
Faltas_Casa = linha["Faltas_Casa"]
Faltas_Fora = linha["Faltas_Fora"]
CA_Casa = linha["CA_Casa"]
CA_Fora = linha["CA_Fora"]
CV_Casa = linha["CV_Casa"]
CV_Fora = linha["CV_Fora"]
Escanteios_Casa = linha["Escanteios_Casa"]
Escanteios_Fora = linha["Escanteios_Fora"]
Impedimentos_Casa = linha["Impedimentos_Casa"]
Impedimentos_Fora = linha["Impedimentos_Fora"]

# -------------- PARTE 1 --------------
# Time da Casa
Casa_limite_forca = r.randint(1,100)
Casa_forca_de_ataque = 0

for x in range(1, Casa_limite_forca+1):
    Casa_forca_de_ataque += x

Casa_gol = Casa_forca_de_ataque//10

# Time de Fora
Fora_limite_forca = r.randint(1,100)
Fora_forca_de_ataque = 0

for x in range(1, Fora_limite_forca+1):
    Fora_forca_de_ataque += x

Fora_gol = Fora_forca_de_ataque//10

# Time vencedor
if Fora_gol > Casa_gol:
    print(f"\n{TimeFora} venceu!")
elif Fora_gol < Casa_gol:
    print(f"\n{TimeCasa} venceu!")
else:
    print("\nOs times empataram!")
print(f"Gols do {TimeCasa}: {Casa_gol} \nGols do {TimeFora}: {Fora_gol}")

# -------------- PARTE 2 --------------
# 1. Aproveitamento

if Chutes_Casa != 0:
    aproveitamento_casa = (Casa_gol/Chutes_Casa)*100
if Chutes_Fora != 0:
    aproveitamento_fora = (Fora_gol/Chutes_Fora)*100
print(f"\nAproveitamento do {TimeCasa}: {aproveitamento_casa:.2f}% \nAproveitamento do {TimeFora}: {aproveitamento_fora:.2f}%")

# 2. Time mais agressivo
agressividade_Casa = (Faltas_Casa)+2*(CA_Casa)+3*(CV_Casa)
agressividade_Fora = (Faltas_Fora)=2*(CA_Fora)+3*(CV_Fora)
print(f"\nAgressividade:\n{TimeCasa}: {agressividade_Casa}\n{TimeFora}: {agressividade_Fora}")
if agressividade_Casa > agressividade_Fora:
    print(f"{TimeCasa} foi mais agressivo.")
elif agressividade_Casa < agressividade_Fora:
    print(f"{TimeFora} foi mais agressivo.")
else:
    print(f"Ambos tiveram a mesma agressividade.")

# 3. Escanteios
print(f"\nEscanteios: \n{TimeCasa}: {Escanteios_Casa} \n{TimeFora}: {Escanteios_Fora}")

diferenca = Escanteios_Casa - Escanteios_Fora
if diferenca < 0:
    diferenca *= -1

if Escanteios_Casa > Escanteios_Fora:
    print(f"{TimeCasa} teve mais escanteios.")
elif Escanteios_Casa < Escanteios_Fora:
    print(f"{TimeFora} teve mais escanteios.")
else:
    print("Empate de escanteios.")
print(f"Houve uma diferença de {diferenca} escanteios.")

# 4. Pressa ofensiva (ipo = indice_pressa_ofensiva)
ipo_casa = Impedimentos_Casa / (Chutes_Casa + Escanteios_Casa + 1)
ipo_fora = Impedimentos_Fora / (Chutes_Fora + Escanteios_Fora + 1)
print(f"\nÍndice de Pressa Ofensiva (IPO):\n{TimeCasa}: {ipo_casa:.2f}% \n{TimeFora}: {ipo_fora:.2f}%")

# -------------- PARTE 3 --------------
# Pressão Time da Casa
limite_pressao_casa = r.randint(50,150)
pressao_casa = 0
ciclos_casa = 0

while pressao_casa < limite_pressao_casa:
    pressao_casa += (Escanteios_Casa * 1.5) + (Chutes_Casa * 1.2) - (Faltas_Fora * 0.5)
    ciclos_casa += 1
print(f"\n{TimeCasa}:\nCiclos suportados: {ciclos_casa}\nPressão máxima suportada: {pressao_casa}\nPressão limite: {limite_pressao_casa}")

# Pressão Time de Fora
limite_pressao_fora = r.randint(50,150)
pressao_fora = 0
ciclos_fora = 0

while pressao_fora < limite_pressao_fora:
    pressao_fora += (Escanteios_Fora * 1.5) + (Chutes_Fora * 1.2) - (Faltas_Fora * 0.5)
    ciclos_fora += 1
print(f"\n{TimeFora}:\nCiclos suportados: {ciclos_fora}\nPressão máxima suportada: {pressao_fora}\nPressão limite: {limite_pressao_fora}")

# Os dados abaixo são dos principais tópicos elencados pelo portal Periódicos Capes quando entro com as
# palavras - chaves: "Urban Ecosystem Services" AND "Remote Sensing". Em uma primeira busca apenas com
# as referidas palavras chaves, são retornados 6.844 resultados.
# Mostrando somente "Periodicos Revisados por Pares" e Refinando para "Artigos" com tópico "Remote Sensing"
# para o range de 2015-2020, são retornados 4.238 artigos. Organizando em excel os principais tópicos a partir
# desse refinamento a partir de 2015, 2016, 2017, 2018, 2019 e 2020 é possível inferir quantos artigos foram adicionados
# em cada tópico nos últimos anos. A seleção abaixo refere-se somente aos 10 principais tópicos em ordem decrescente
# iniciando pelo ano de 2020 e desempatando pela ordem dos anos anteriores(2019, 2018, 2017, 2016, 2015).
# Ou seja, buscou-se a partir dos principais tópicos de pesquisa em que as palavras chaves aparecem no ano de 2020
# entender sua evolução desde 2015.

import matplotlib.pyplot as plt

Ano = [2015, 2016, 2017, 2018, 2019, 2020]
Geography = [90,82,72,103,109,30]
Land_Use = [81,65,58,93,101,23]
Landsat = [50,36,46,45,68,17]
Satellite_Imagery = [30,26,40,35,68,15]
Climate_Change = [37,22,32,45,52,13]
Mapping = [46,37,30,27,40,13]
Land_Cover = [31,29,33,46,60,11]
Agricultural_Land = [0,0,0,0,39,11]
Machine_Learning = [0,0,0,0,21,11]
China = [29,19,22,51,65,10]

plt.figure( figsize=(10, 8) )


plt.plot(Ano, Geography, "lightgreen", linewidth=1.0,
         label="Geografia")
plt.plot(Ano, Land_Use, "purple", linewidth=2.0,
         label="Uso do solo")
plt.plot(Ano, Landsat, "red", linewidth=2.0,
         label="Landsat")
plt.plot(Ano, Satellite_Imagery, "black", linewidth=2.0,
         label="Imagem de satélite")
plt.plot(Ano, Climate_Change, "yellow", linewidth=2.0,
         label="Mudança climática")
plt.plot(Ano, Mapping, "pink", linewidth=2.0,
         label="Mapeamento")
plt.plot(Ano, Land_Cover, "brown", linewidth=2.0,
         label="Mapeamento")
plt.plot(Ano, Agricultural_Land,"darkgreen", linewidth=2.0,
         label="Área agrícola")
plt.plot(Ano, Machine_Learning, "darkblue", linewidth=2.0,
         label="Machine Learning")
plt.plot(Ano, China, "lightblue", linewidth=2.0,
         label="China")

plt.xlim([2015, 2020])
plt.ylim([0, 120])

plt.title("""Principais tópicos publicando pesquisas sobre 
'Serviços Ecossistemicos Urbanos' e 'Sensoriamento Remoto' desde 2015
Fonte: http://www.periodicos.capes.gov.br/""",size=15)

plt.legend(ncol = 2)


plt.xlabel("Ano",size=12)
plt.ylabel("Número de artigos publicados",size=12)


plt.grid(b=True, color='gray', linestyle='-.', linewidth=1)

plt.show()
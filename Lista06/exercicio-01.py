# encoding: utf-8

# importanto a biblioteca numpy
import numpy as np

# inserindo as séries em arranjos matriciais

s1 = np.array((168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 323, 106, 1055, 170))
s2 = np.array((168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 180, 106, 1055, 200))

# subtraindo termos das séries S2 - S1
subtracao = s2-s1
# print("subtracao\n",subtracao)
# definindo o quadrado de cada subtração
quadrado = subtracao * subtracao
# print("quadrado\n",quadrado)
# aplicando somatório de cada termo na matriz 'quadrado'
somatorio = np.sum(quadrado)
# print("somatorio\n",somatorio)
# extraindo a raíz do somatorio
distancia_euclidiana = np.sqrt(somatorio)

print("distancia euclidiana: ",distancia_euclidiana)

# com valor da serie previamente definido, calcula-se em duas etapas
# soma das séries
soma_serie = s1 + s2
# print("soma\n", soma_serie)
# média das séries
media = soma_serie/2
print("Serie temporal com valores medios:\n", media)

# organizando as séries em um DataFrame
series_mistas = np.array((s1,s2))
# print("serie 1 e 2 em um data frame\n",series_mistas)

# atribuindo valor máximo do eixo 0, nas colunas
serie_max = series_mistas.max(axis=0)
print("serie com valores maximos:\n",serie_max)

# atribuindo valor mínimo do eixo 0, nas colunas
serie_min = series_mistas.min(axis=0)
print("serie com valores mínimos:\n",serie_min)


# encoding: utf-8

#importando matplotlib

import matplotlib

#importando submodulo pyplot do matplotlib como plt

import matplotlib.pyplot as plt

#definindo os eixos idade e tamanho da população feminina para cada idade como listas
Idade = [ "0 a 4"," 5 a 9" , " 10 a 14" , " 15 a 19" , " 20 a 24" , " 25 a 29" , " 30 a 34" , " 35 a 39" , " 40 a 44" , " 45 a 49" , " 50 a 54" ," 55 a 59" ," 60 a 64" ," 65 a 69" ," 70 a 74" ," 75 a 79" ," 80 a 84" ," 85 a 89" ," 90 a 94" ," 95 a 99" ," >=100 "]
Pop_Feminina = [6779171,7345231,8441348,8432004,8614963,8643419,8026854,7121915,6688796,6141338,5305407,4373877,3468085,2616745,2074264,1472930,998349,508724,211594,66806,16989]

# criando uma lista com a posição de cada idade
x_pos = [ x for x in range(len(Idade)) ]

# definindo tamanho da figura
plt.figure( figsize=(10, 8) )

# definindo valores dos eixos horizontal (x_pos) e vertical (Pop_feminina) e outroas atributos
plt.bar(x_pos, Pop_Feminina, align='center',
        color='Purple', linewidth=2, edgecolor='black')

# definindo labels para eixo x e y, sendo y expresso em milhões (M)
plt.xticks(x_pos, Idade, rotation=45)
plt.yticks([ 2e6, 4e6, 6e6, 8e6 ],
           [ '2M', '4M', '6M', '8M' ] )

# definindo título do gráfico e tamanho da fonte
plt.title("Distribuição de mulheres por grupos de idade - Brasil",size=20)

# definindo título dos exiso horizontal e vertical e tamanho da respectiva fonte
plt.xlabel("Idade (anos)",size=16)
plt.ylabel("Número de mulheres",size=16)

#definindo características do grid
plt.grid(b=True, color='gray', linestyle='-.', linewidth=1)

plt.show()
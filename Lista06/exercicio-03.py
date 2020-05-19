# encoding: utf-8

import matplotlib.pyplot as plt

# similar ao exercicio 2, mas veja a mudança nos comentários

Idade = [ "0 a 4"," 5 a 9" , " 10 a 14" , " 15 a 19" , " 20 a 24" , " 25 a 29" , " 30 a 34" , " 35 a 39" , " 40 a 44" , " 45 a 49" , " 50 a 54" ," 55 a 59" ," 60 a 64" ," 65 a 69" ," 70 a 74" ," 75 a 79" ," 80 a 84" ," 85 a 89" ," 90 a 94" ," 95 a 99" ," >=100 "]

Pop_Masculina = [7016987,7624144,8725413,8558868,8630229,8460995,7717658,6766664,6320568,5692014,4834995,3902344,3041035,2224065,1667372,1090517,668623,310759,114964,31529,7247]

y_pos = [ y for y in range(len(Idade)) ]

plt.figure( figsize=(10, 8) )

# plotando os valroes do eixo vertical, horizontal e demais atributos
plt.barh(y_pos,Pop_Masculina, align='center',
        color='Darkgray', linewidth=2, edgecolor='black')

# plotando os rótulos do eixo vertical, horizontal e demais atributos
plt.yticks(y_pos, Idade, rotation=45)
plt.xticks([ 2e6, 4e6, 6e6, 8e6 ],
           [ '2M', '4M', '6M', '8M' ] )

plt.title("Distribuição de homens por grupos de idade - Brasil",size=20)

plt.xlabel("Número de homens",size=16)
plt.ylabel("Idade (anos)",size=16)

plt.grid(b=True, color='gray', linestyle='-.', linewidth=1);

plt.show()
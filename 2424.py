'''
Una cancha de tenis tiene la forma de un rectángulo, cuyos lados miden 36 pies por 78 pies, que corresponden a un rectángulo que mide 432 pulgadas por 936 pulgadas. En el último Grand Slam de Australia, Rafael Nadal perdió ante Novak Djoković, en uno de los partidos de tenis más bellos de los últimos tiempos.

A menudo, una jugada es tan rápida y la pelota está tan cerca del borde de la cancha que el árbitro puede tomar una decisión que puede ser impugnada por uno de los jugadores. Para ello, existe un desempate, que utiliza la imagen grabada del partido para decidir si el balón estaba dentro o fuera de la mitad de la cancha correspondiente a uno de los jugadores.

Considere que el semicuadrante de Rafael Nadal corresponde a un rectángulo en el que dos vértices tienen coordenadas (0,0) y (432, 468), donde todos los números están en pulgadas.

Debe escribir un programa para, dadas las coordenadas (X, Y ) del punto de contacto de la pelota con el suelo, determinar si una pelota golpeó el suelo dentro o fuera de la semicancha. Tenga en cuenta que si la pelota golpea la línea divisoria, se considera una bola de entrada.

Entrada
La entrada se da en una sola línea, que contiene dos números enteros X e Y (-500 ≤ X, Y ≤ 500), que corresponden a las coordenadas del punto (X, Y ) de contacto de la pelota con el suelo, en pulgadas.

Salida
Su programa debe imprimir una sola línea, que contenga la palabra si la pelota golpea dentro de la mitad de la cancha y la palabra si no.'''


n = list(map(int,input().rstrip().split()))

if n[0] < 0 or n[1] < 0 or n[0] > 432 or n[1] > 468:
   print('fora')
else:
   print('dentro')
   
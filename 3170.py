'''¡A Amelia le encanta la Navidad y su parte favorita en esta fecha es armar el árbol de Navidad! Le encanta decorar el árbol con lunares y luces de colores, ¡para que se vea brillante y divertido! Sin embargo, a Amélia le gustan las cosas bien distribuidas y exige que su árbol no tenga más de la mitad de las ramas en bolas. Entonces, 
** si su árbol de Navidad tiene ramas G, necesita canicas G/2. 
** Si el número G de ramas es impar, ese valor se redondeará hacia abajo.
Este año, Amélia decidió actualizar su árbol y comprará uno nuevo. Además, algunas de sus bolas se rompieron y necesitará saber cuántas bolas nuevas necesitará comprar para mantener su árbol equilibrado como a ella le gusta.

¡Para eso, ella quiere tu ayuda! Dada la cantidad de bolas que tiene Amelia y la cantidad de ramas que tendrá su nuevo árbol, ¡dígale a Amelia cuántas bolas de Navidad necesita comprar para decorar su nuevo árbol!

Input
La entrada consta de dos valores enteros, leídos en dos líneas, B (1 < B < 103) y G (100 < G < 1000) que indican, respectivamente, el número de bolas que ya tiene Amélia y el número de ramas de su nuevo Árbol de Navidad.

Output
Imprime la cantidad de pelotas que Amélia necesita comprar para completar su árbol, con el mensaje "Faltam B bolinha(s)" (en inglés, Missing B ball(s)), donde B es la cantidad de pelotas que Amelia necesita comprar. Si Amelia tiene suficientes bolas de sobra, imprime el mensaje "¡Amelia tem todas bolinhas!" (en inglés, "¡Amelia tiene todas las pelotas!")
'''

a = int(input())
b = int(input())

if b % 2 == 1:
   b = b-1

faltan = (b/2)-a

if faltan > 0:
   print(f'Faltam {faltan:.0f} bolinha(s)')
else:
   print('Amelia tem todas bolinhas!')


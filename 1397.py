'''
A Og le encanta jugar con sus hijos. Su juego favorito es el juego de los más grandes, inventado por él mismo. Este pasatiempo (había mucho tiempo disponible para jugar en la era de los hombres de las cavernas) lo juegan dos jugadores, Og y uno de sus hijos. Las reglas del juego son las siguientes: Primero, los jugadores eligen el número de rondas del partido. Durante una ronda, cada jugador grita un número entre 0 y 10. El jugador que grita el mayor número gana un punto (en caso de empate, nadie gana). Después de todas las rondas, se cuentan los puntos y gana el jugador que tiene la mayor puntuación.

A Og y sus hijos les gusta mucho este juego, pero por lo general se pierden con las matemáticas. ¿Ayudarás a Og a determinar la puntuación final?

Entrada
La entrada consta de varios casos de prueba (coincidencias). Cada caso de prueba comienza con un número entero N (1 ≤ N ≤ 10) que describe el número de rondas del partido. El valor N = 0 indica el final de la entrada y no debe procesarse. Las siguientes N líneas contienen dos números enteros A y B cada uno (0 ≤ A, B ≤ 10). A es el número que grita el primer jugador durante la ronda y B es el número que grita el segundo jugador durante la ronda.

Salida
La salida debe contener una línea para cada caso de prueba. Esta línea contiene la puntuación de los jugadores, separados por un solo espacio.
'''


n = int(input())
lista = []
while n != 0:
   a = 0
   b = 0
   for i in range(n):
      l = list(map(int,input().rstrip().split()))
      if l[0] > l[1]:
         a+=1
      elif l[1]> l[0]:
         b+=1
      else:
         pass
   lista.append(f'{a} {b}')
   a = 0
   b = 0
   n = int(input())

for i in lista:
   print(i)
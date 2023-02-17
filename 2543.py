'''
Como muchos estudiantes de Informática, te gusta jugar a los juegos electrónicos más populares hoy en día: Ligue of Leyends (LOL) y Counter-Strike (CS). Aunque también juegas LOL, 
¡lo que realmente te gusta hacer es usar todas tus habilidades para derrotar a las fuerzas terroristas en Contra-Strike! Eres tan bueno combatiendo el terrorismo que a menudo se te 
compara con el presidente de los EE. UU. que anunció la captura de un famoso terrorista de la vida real.

Como tus habilidades son incomparables, los videos de tus partidos (tus famosos gameplays) aparecen a menudo en UFPR Gaming, una página web que publica los gameplays de los estudiantes 
de nuestra universidad.

La página publica muchos videos todos los días. Por lo tanto, puede ser difícil encontrar y contar todos tus videos ya publicados. Sin embargo, como también eres programador, decidiste 
escribir un programa de computadora para ayudarte con esta tarea. Dada la lista de partidas publicadas por la página, determine cuántos de ellos son videos de usted jugando Contra-Strike.

Input
La entrada contiene varios casos de prueba. La primera línea de cada caso de prueba contiene dos números enteros N e I (1 ≤ N ≤ 104, 1000 ≤ I ≤ 9999), el número de partidas publicadas 
por la página y el ID de tu universidad, respectivamente.

Las siguientes N líneas describen los videos publicados. Cada juego se describe con dos números enteros i y j (1000 ≤ i ≤ 9999, j=0 o 1), donde i es el ID de la universidad del autor 
y j=0 si el juego es uno de Contra-Strike, o j=1 si es una Liga de Legendas.

La entrada termina con fin de archivo (EOF).

Output
Para cada caso de prueba, imprima una sola línea que contenga un número que indique cuántos videos suyos jugando Contra-Strike fueron publicados por la página.'''

while True:
   try:
      n = list(map(int,input().rstrip().split()))
      suma = 0
      for i in range(n[0]):
         l = list(map(int,input().rstrip().split()))
         if n[1] == l[0] and l[1] == 0:
            suma+=1
      print(suma)
   except EOFError: break


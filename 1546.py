'''
Varios estudiantes de diversas universidades conocen el portal de programación IRU. Este portal tiene miles de problemas de programación disponibles. Diariamente, el equipo de IRU recibe varios comentarios (felicitaciones, errores, preguntas, sugerencias, ...) que primero deben asignarse a los miembros del equipo para responder.

Como el equipo está muy ocupado y no tiene tiempo para clasificar estos comentarios, se le pidió que escribiera un programa para hacer eso y mostrar quién será responsable de resolver y responder los comentarios.

Los miembros del equipo responsables de cada sector son:

   Cumplidos: Rolien
   Errores: Naej
   Preguntas: Elehcim
   Sugerencias: Odranoel

Entrada
El primer valor es el número de casos de prueba N (1 < N < 100). Cada caso de prueba representa un día de trabajo respondiendo feedbacks. Cada caso de prueba comienza con K (1 < K < 50), lo que indica el número de comentarios recibidos en esa fecha. Luego sigue K líneas con un número entero que representa la categoría de cada una de las retroalimentaciones como se muestra arriba (1, 2, 3 o 4).

Salida
Para cada caso de prueba, debe imprimir el nombre del miembro del equipo responsable de la retroalimentación.
'''

n = int(input())
lista = []
for i in range(n):
   m = int(input())
   for i in range(m):
      c = int(input())
      if c == 1:
         lista.append('Rolien')
      elif c == 2:
         lista.append('Naej')
      elif c == 3:
         lista.append('Elehcim')
      elif c == 4:
         lista.append('Odranoel')

for i in lista:
   print(i)
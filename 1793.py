'''Las escaleras mecánicas han facilitado mucho la vida de las personas. Subir escaleras es una de las tareas más aburridas jamás inventadas (después de la invención de las escaleras en primer lugar).

Después de algunas observaciones, se dio cuenta de que se gasta mucha energía con las escaleras mecánicas, porque continúan funcionando incluso cuando no hay nadie usándolas. Para evitar eso, el dueño de un centro comercial local instaló un sensor que verifica cuando hay alguien en la escalera mecánica. Cuando el sensor no detecta presencia, la escalera mecánica se desactiva, ahorrando así energía hasta que llegue la siguiente persona.

Para ser más precisos, el sistema funciona de la siguiente manera: la escalera mecánica está inicialmente inactiva. El tiempo que tarda una persona en ir desde el principio hasta el final de la escalera mecánica es de 10 segundos. Es decir, si una persona llega a la escalera mecánica en el tiempo t, la escalera mecánica estará activa en los tiempos t, t+1, t+2, …, t+8 y t+9, y luego se desactivará en el tiempo t. +10, cuando la persona sale de la escalera mecánica. Dicha ventana de tiempo puede prolongarse si una o más personas llegan a la escalera mecánica durante dicho proceso.

El dueño del centro comercial local ahora pidió tu ayuda. Escriba un algoritmo que, dadas las horas en que algunas personas llegaron a la escalera mecánica, diga cuántos segundos estuvo activa la escalera mecánica.

Input
Habrá como máximo 30 casos de prueba. Cada caso de prueba comienza con una línea que contiene un número entero N, que representa el número de personas que usaron la escalera mecánica ese día (1 ≤ N ≤ 100).
En la siguiente línea habrá N números enteros distintos, dados en orden ascendente, que representan el tiempo t en el que cada persona llegó a la escalera mecánica (1 ≤ t ≤ 1000).
El último caso de prueba se indica cuando N = 0, que no debe procesarse.

Output
Para cada caso de prueba, imprima una línea, que contenga un número entero, que represente cuántos segundos estuvo activa la escalera mecánica.'''

i = int(input())

segundos = []
while i > 0:
   a = input()
   casos = list(map(int,a.rstrip().split(" ")))
   if len(casos) == 1:
      segundos.append(10)
   else:
      segundo = 0
      for i in range(len(casos)-1):
         if (casos[i+1]-casos[i])>10:
            segundo+=10

         elif (casos[i+1]-casos[i])<=10:
            segundo+=((casos[i+1]-casos[i]))

      segundo+=10
      segundos.append(segundo)
      segundo=0

   i = int(input())

for i in segundos:
   print(i)

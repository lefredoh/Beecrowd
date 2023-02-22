'''
Su profesor desea hacer un programa con las siguientes características:
   Lea 10 nombres, sin espacio en blanco;
   Imprima el tercer nombre de la lista;
   Imprima el séptimo nombre de la lista;
   Imprima el noveno nombre de la lista.

Entrada
La entrada consta de varios archivos de prueba. En cada archivo de prueba hay diez líneas. En cada línea tiene un nombre de no más de 30 caracteres y sin espacio en blanco. Como se muestra en el siguiente ejemplo de entrada.

Salida
Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene tres líneas según los procedimientos 2, 3 y 4. Como se muestra en el siguiente ejemplo de salida.
'''


lista = []
for i in range(1,11):
   n = input()
   if i == 3 or i == 7 or i ==9:
      lista.append(n)

for i in lista:
   print(i)
   
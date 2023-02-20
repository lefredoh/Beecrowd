'''
Su profesor desea hacer un programa con las siguientes características:

   Lea un número en el formato: XXXXX.YYY;
   Imprima el número en la forma invertida: YYY.XXXXX.

Entrada
La entrada consta de varios archivos de prueba. En cada archivo de prueba tiene una línea. La línea tiene un número real con 3 decimales. Como se muestra en el siguiente ejemplo de entrada.

Salida
Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene una línea de la forma descrita en los elementos 2. Como se muestra en el siguiente ejemplo de salida.
'''

n = input()
a = int(n.split('.')[0])
b = int(n.split('.')[1])
print(f'{b}.{a}')


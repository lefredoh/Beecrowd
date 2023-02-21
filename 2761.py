'''
Su profesor desea hacer un programa con las siguientes características:

   Cree una variable entera;
   Cree una variable real de simple precisión;
   Cree una variable que almacene un carácter;
   Cree una variable que almacene una frase de un máximo de 50 caracteres;
   Lea todas las variables en el orden de la forma creada;
   Imprima todas las variables como se leyeron;
   Imprima las variables, separándolas por una tabulación (8 espacios), en el orden que se leen;
   Imprima las variables con exactos 10 espacios.

Entrada
La entrada consta de varios archivos de prueba. En cada archivo de prueba tiene una línea. La línea tiene una variable A que almacena un entero, una variable B que almacena un número real, una variable C con un carácter y una variable D que almacena una frase de un máximo de 50 caracteres. Como se muestra en el siguiente ejemplo de entrada.

Salida
Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene tres líneas de la forma descrita en los apartados 6, 7 y 8. Como se muestra en el siguiente ejemplo de salida. Imprima los valores de punto flotante con 6 decimales después de la coma.
'''

from struct import pack, unpack
e = str(input())
a = e[:e.find(' ')]
e = e[e.find(' ')+1:]
f = e[:e.find(' ')]
b = e[:e.find(' ')]
e = e[e.find(' ')+1:]
c = e[0]
d = e[e.find(' ')+1:]
fl = float(unpack('f', pack('f', float(f)))[0])
b = '{:10.6f}'.format(fl).replace(' ', '')
print(str(a)+str(b)+str(c)+str(d))
print(f'{a}\t{b}\t{c}\t{d}')
print('{:>10}{:>10}{:>10}{:>10}'.format(a, b, c, d))



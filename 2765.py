'''
Su profesor desea hacer un programa con las siguientes características:

   Lea una frase que va a tener una virgula en el medio del texto;
   Imprima la primera parte de la frase;
   Imprima la segunda parte de la frase.

Entrada
La entrada consta de varios archivos de prueba. En cada archivo de prueba tiene una línea. La línea tiene una frase con un máximo de 100 caracteres (puede tener espacio en blanco) y una coma. Como se muestra en el siguiente ejemplo de entrada.

Salida
Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene dos líneas según los pasos 2 y 3. Como se muestra en el siguiente ejemplo de salida.
'''

t = input().replace(',','\n')
print(t)
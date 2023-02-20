'''Entrada y Salida de String

Por Roberto A. Costa Jr, UNIFEI BR Brazil
Timelimit: 1

Su profesor desea hacer un programa con las siguientes características:

   Cree 3 variables para almacenar una frase de un máximo de 100 caracteres;
   Lea una frase para la primera variable;
   Lea una frase para la segunda variable;
   Lea una frase para la tercera variable;
   Imprima la primera variable leída en el paso 2, la segunda variable leída en el paso 3, la tercera variable leída en el paso 4. No olvide saltar línea;
   Imprima la primera variable leída en el paso 3, la segunda variable leída en el paso 4, la tercera variable leída en el paso 2. No olvide saltar línea;
   Imprima la primera variable leída en el paso 4, la segunda variable leída en el paso 2, la tercera variable leída en el paso 3. No olvide saltar línea;
   Repita el procedimiento 5, imprimiendo sólo 10 caracteres de cada variable.

Entrada

La entrada consta de varios archivos de prueba. En cada archivo de prueba tiene tres líneas. En la primera línea tiene una variable A que almacena una frase de un máximo de 100 caracteres. En la segunda línea tiene una variable B que almacena una frase de no más de 100 caracteres. En la tercera línea tiene una variable C que almacena una frase de un máximo de 100 caracteres. Como se muestra en el siguiente ejemplo de entrada.
Salida

Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene cuatro líneas de la forma descrita en los apartados 5, 6, 7 y 8. Como se muestra en el siguiente ejemplo de salida.
'''

a = input()
b = input()
c = input()
print(a+b+c)
print(b+c+a)
print(c+a+b)
print(a[:10]+b[:10]+c[:10])

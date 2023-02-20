'''
Su profesor desea hacer un programa con las siguientes características:

   Cree 3 variables para almacenar un único carácter;
   Lea un valor de carácter para la primera variable;
   Lea un valor de carácter para la segunda variable;
   Lea un valor de carácter para la tercera variable;
   Imprima la letra A, un espacio en blanco, el signo igual, un espacio en blanco, el carácter almacenado en la primera variable leída en el paso 2, una virgula, un espacio en blanco, la letra B, un espacio en blanco, el signo de igual, un espacio en blanco, el carácter almacenado en la segunda variable leída en el paso 3, la letra C, un espacio en blanco, el signo igual, un espacio en blanco, el carácter almacenado en la tercera variable leída en el paso 4. No olvida saltar la línea;
   Imprima la letra A, un espacio en blanco, el signo igual, un espacio en blanco, el carácter almacenado en la primera variable leída en el paso 3, una virgula, un espacio en blanco, la letra B, un espacio en blanco, el signo de un espacio en blanco, el carácter almacenado en la segunda variable leída en el paso 4, la letra C, un espacio en blanco, el signo igual, un espacio en blanco, el carácter almacenado en la tercera variable leída en el paso 2. No olvida saltar la línea;
   Imprima la letra A, un espacio en blanco, el signo igual, un espacio en blanco, el carácter almacenado en la primera variable leída en el paso 4, una virgula, un espacio en blanco, la letra B, un espacio en blanco, el signo de igual, un espacio en blanco, el carácter almacenado en la segunda variable leída en el paso 2, la letra C, un espacio en blanco, el signo igual, un espacio en blanco, el carácter almacenado en la tercera variable leída en el paso 3. olvídate de saltar la línea.

Entrada

La entrada consta de varios archivos de prueba. En cada archivo de prueba tiene tres líneas. En la primera línea tiene una variable A que almacena un valor de carácter. En la segunda línea tiene una variable B que almacena un valor de carácter. En la tercera línea tiene una variable C que almacena un valor de carácter. Como se muestra en el siguiente ejemplo de entrada.
Salida

Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene tres líneas de la forma descrita en los puntos 5, 6 y 7. Como se muestra en el siguiente ejemplo de salida.
'''

a = input()
b = input()
c = input()
print(f'A = {a}, B = {b}, C = {c}')
print(f'A = {b}, B = {c}, C = {a}')
print(f'A = {c}, B = {a}, C = {b}')

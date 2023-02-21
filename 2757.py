'''
Su profesor le gustaría que usted hiciera un programa con las siguientes características:

   Cree tres variables para almacenar números enteros;
   Lea el primer número, que puede ser un valor en el rango de: -10000 ≤ A ≤ 10000;
   Lea el segundo número, que puede ser un valor en el rango de: 0 ≤ B ≤ 99;
   Lea el tercer número, que puede ser un valor en el rango de: 0 ≤ C ≤ 999;
   Imprima la letra A, un espacio en blanco, el signo igual, un espacio en blanco, el número almacenado en la primera variable, una virgula, un espacio en blanco, la letra B, un espacio en blanco, el signo igual, espacio en blanco, el número almacenado en la segunda variable, una virgula, un espacio en blanco, la letra C, un espacio en blanco, el signo igual, un espacio en blanco, el número almacenado en la tercera variable. No olvide saltar la línea;
   Repita el procedimiento 5, colocando el número en un espaciado de 10 dígitos y justificado a la derecha;
   Repita el procedimiento 5, colocando el número en un espaciado de 10 dígitos y rellenado con ceros;
   Repita el procedimiento 5, colocando el número en un espaciado de 10 dígitos y justificado a la izquierda.

Entrada

La entrada consta de varios archivos de prueba. En cada archivo de prueba tiene tres líneas. En la primera línea tiene un entero A (-10000 ≤ A ≤ 10000). En la segunda línea tiene un entero B (0 ≤ B ≤ 99). En la tercera línea tiene un entero C (0 ≤ C ≤ 999). Como se muestra en el siguiente ejemplo de entrada.
Salida

Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene cuatro líneas de la forma descrita en el apartado 5. Como se muestra en el siguiente ejemplo de salida.


'''

a = int(input())
b = int(input())
c = int(input())

print(f'A = {a}, B = {b}, C = {c}')
print(f'A = {a:10d}, B = {b:10d}, C = {c:10d}')
print(f'A = {a:010d}, B = {b:010d}, C = {c:010d}')
print(f'A = {a:<10d}, B = {b:<10d}, C = {c:<10d}')

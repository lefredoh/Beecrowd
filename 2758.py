'''
Su profesor desea hacer un programa con las siguientes características:
   Cree dos variables para almacenar números reales de precisión simple;
   Cree dos variables para almacenar números reales de precisión doble;
   Lea el primer número de precisión simple que siempre tendrá un decimal;
   Lea el segundo número de precisión simple que siempre tendrá dos decimales;
   Lea el primer número de doble precisión que siempre tendrá tres decimales;
   Lea el segundo número de precisión doble que siempre tendrá cuatro decimales;
   Imprima la letra A, un espacio en blanco, el signo igual, un espacio en blanco, el número almacenado en la primera variable leída en el paso 3, una virgula, un espacio en blanco, la letra B, un espacio en blanco, de igual, un espacio en blanco, el número almacenado en la segunda variable leída en el paso 4. No olvide saltar línea;
   Imprima la letra C, un espacio en blanco, el signo igual, un espacio en blanco, el número almacenado en la primera variable leída en el paso 5, una virgula, un espacio en blanco, la letra D, un espacio en blanco, de igual, un espacio en blanco, el número almacenado en la segunda variable leída en el paso 6. No olvide saltar línea;
   Repita el procedimiento 7, imprimiendo los números con un decimal;
   Repita el procedimiento 8, imprimiendo los números con un decimal;
   Repita el procedimiento 7, imprimiendo los números con dos decimales;
   Repita el procedimiento 8, imprimiendo los números con dos decimales;
   Repita el procedimiento 7, imprimiendo los números con tres decimales;
   Repita el procedimiento 8, imprimiendo los números con tres decimales;
   Repita el procedimiento 7, imprimiendo los números con tres decimales y en forma de notación científica con el carácter E;
   Repita el procedimiento 8, imprimiendo los números con tres decimales y en forma de notación científica con el carácter E;
   Repita el procedimiento 7, imprimiendo solamente la parte entera del número;
   Repita el procedimiento 8, imprimiendo solamente la parte entera del número.
Entrada
La entrada consta de varios archivos de prueba. En cada archivo de prueba tiene dos líneas. En la primera línea tiene dos números reales A y B (-1000.0 ≤ A, B ≤ 1000.0), separados por espacio en blanco. En la segunda línea tiene dos números reales C y D (-1000.0 ≤ C, D ≤ 1000.0), separados por espacio en blanco. Como se muestra en el siguiente ejemplo de entrada.

Salida
Para cada archivo de la entrada, tendrá un archivo de salida. El archivo de salida tiene doce líneas de la forma descrita en el ítem 7 y 8. Como muestra el siguiente ejemplo de salida.
'''
from struct import pack, unpack
A = list(map(float,input().rstrip().split()))
B = list(map(float,input().rstrip().split()))
a = float(unpack("f", pack("f", float(A[0])))[0])
b = float(unpack("f", pack("f", float(A[1])))[0])
c = B[0]
d = B[1]

print(f'''A = {a:.6f}, B = {b:.6f}
C = {c:.6f}, D = {d:.6f}
A = {a:.1f}, B = {b:.1f}
C = {c:.1f}, D = {d:.1f}
A = {a:.2f}, B = {b:.2f}
C = {c:.2f}, D = {d:.2f}
A = {a:.3f}, B = {b:.3f}
C = {c:.3f}, D = {d:.3f}
A = {a:.3E}, B = {b:.3E}
C = {c:.3E}, D = {d:.3E}
A = {a:.0f}, B = {b:.0f}
C = {c:.0f}, D = {d:.0f}''')


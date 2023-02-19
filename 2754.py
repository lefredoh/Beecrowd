'''
Su profesor le gustaría que usted hiciera un programa con las siguientes características:

   Cree dos variables reales de doble precisión;
   Asigne la primera el valor 234.345 y la segunda el valor 45.698;
   Imprima las dos variables con seis decimales;
   Imprima las dos variables sin ningún decimal;
   Imprima las dos variables con un decimal;
   Imprima las dos variables con dos decimal;
   Imprima las dos variables con tres decimal;
   Imprima las dos variables con notación científica con 'e';
   Imprima las dos variables con notación científica con 'E';
   Imprime las dos variables con la representación más corta, con 'e' o 'E' o sin;
   Imprime las dos variables con la representación más corta, con 'e' o 'E' o sin;

Para imprimir, separe los valores con un espacio en blanco, un rastro (-) y un espacio en blanco.
Entrada

No hay.
Salida

El resultado de su programa debe ser escrito según el ejemplo de la salida.
'''

a = 234.345
b = 45.698

print(f'{a:.6f} - {b:.6f}')
print(f'{a:.0f} - {b:.0f}')
print(f'{a:.1f} - {b:.1f}')
print(f'{a:.2f} - {b:.2f}')
print(f'{a:.3f} - {b:.3f}')
print(f'{a/100:.6f}e+02 - {b/10:.6f}e+01')
print(f'{a/100:.6f}E+02 - {b/10:.6f}E+01')
print(f'{a:.3f} - {b:.3f}')
print(f'{a:.3f} - {b:.3f}')
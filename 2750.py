'''

Su profesor de programación le gustaría que usted hiciera un programa con las siguientes características:

   Crear 16 variables enteras;
   Asignar a ellos valores de 0 a 15 a cada una de las variables anteriores;
   Tener 39 rasgos (-) en la primera línea;
   Tener una | en el primer trazo, décimo tercero, vigésimo tercero y del trigésimo noveno trazo de la primera línea, debajo del cuarto trazo debe comenzar a escribir "decimal", debajo del 16º trazo debe comenzar a escribir "octal", debajo del 26º trazo debe comenzar a escribir "octal" escribir "Hexadecimal" y el resto llenar con espacio en blanco;
   Repita el procedimiento 1;
   Tener una | en el primer trazo, décimo tercero, vigésimo tercero y del trigésimo noveno trazo de la primera línea, debajo del octavo trazo, debe imprimir el valor de la primera variable en valor decimal, debajo del décimo octavo traza, debe imprimir el valor de la primera variable en valor octal, debajo del 31º rastro debe imprimir el valor de la primera variable en valor hexadecimal y el resto llenar con espacio en blanco;
   Repita el procedimiento 6 para las otras 15 variables;
   Repita el procedimiento 1.

Al final debe quedar igual a la siguiente imagen:

--------------------------------------- (39 rastros)
|  decimal  |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
--------------------------------------- (39 rastros)
Entrada
No hay.

Salida
La salida se imprimirá según la figura anterior.
'''
print('-'*39)
print('|'+'  decimal  '+'|'+'  octal  '+'|'+'  Hexadecimal'+'  |')
print('-'*39)
for i in range(16):
   e = ' '*6
   if i >9:
      e=' '*5
   o = ' '*4
   if i>7:
      o=' '*3
   h = hex(i)[2:]
   if i>9:
      h = str(h).capitalize()
   print('|'+e+f'{i}    |'+o+oct(i)[2:]+' '*4+'|'+' '*7+h+' '*7+'|')
print('-'*39)

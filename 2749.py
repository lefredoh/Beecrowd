'''
Su profesor desea hacer una pantalla con las siguientes características:
   Tener 39 rasgos (-) en la primera línea;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, debajo del 2º trazo debe comenzar a escribir "x = 35" y el resto llenar con espacio en blanco;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, llenar en el medio con espacio en blanco;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, debajo del 17º trazo debe comenzar a escribir "x = 35" y el resto llenar con espacio en blanco;
   Repita el procedimiento 3;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, debajo del 33º trazo debe comenzar a escribir "x = 35" y el resto llenar en el medio con espacio en blanco;
   Repita el procedimiento 1.
Al final debe quedar igual a la siguiente imagen:
--------------------------------------- (39 traces)
|x = 35                               |
|                                     |
|               x = 35                |
|                                     |
|                               x = 35|
--------------------------------------- (39 traces)

Entrada
No hay.

Salida
La salida se imprimirá según la figura anterior.
'''

print('-'*39)
print('|'+'x = 35'+' '*31+'|')
print('|'+' '*37+'|')
print('|'+' '*15+'x = 35'+' '*16+'|')
print('|'+' '*37+'|')
print('|'+' '*31+'x = 35'+'|')
print('-'*39)

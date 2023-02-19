'''
Su profesor de programación desea hacer una pantalla con las siguientes características:

   Tener 39 rasgos (-) en la primera línea;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, debajo del 10 trazo debe comenzar a escribir la palabra "Roberto" y el resto llenar en el medio con espacio en blanco;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, llenar en el medio con espacio en blanco;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, debajo del 10 rasgo debe comenzar a escribir el número "5786" y el resto llenar en el medio con espacio en blanco;
   Repita el procedimiento 3;
   Tener una | debajo del primer trazo y del trigésimo noveno trazo de la primera línea, debajo del 10 trazo debe comenzar a escribir la palabra "UNIFEI" y el resto llenar en el medio con espacio en blanco;
   Repita el procedimiento 1.

--------------------------------------- (39 traces)
|        Roberto                      |
|                                     |
|        5786                         |
|                                     |
|        UNIFEI                       |
--------------------------------------- (39 traces)
Entrada

No hay.
Salida

La salida se imprimirá según la figura anterior.
'''

print('-'*39)
print('|'+' '*8+'Roberto'+' '*22+'|')
print('|'+' '*37+'|')
print('|'+' '*8+'5786'+' '*25+'|')
print('|'+' '*37+'|')
print('|'+' '*8+'UNIFEI'+' '*23+'|')
print('-'*39)
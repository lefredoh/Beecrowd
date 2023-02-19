'''
Su profesor le gustaría que usted hiciera un programa con las siguientes características:

   Cree veintiséis variables entera;
   Asigne la primera variable el valor 97;
   Asigne las demás demás variables el valor de la primera sumada de una unidad;
   En la pantalla se muestran los valores numéricos de la primera variable, un espacio en braco, el carácter 'e', otro espacio en blanco y su valor alfanumérico (caracteres);
   Repita el procedimiento para todas las demás variables.

Entrada

No hay.
Salida

El resultado de su programa debe ser el mismo del ejemplo de salida.
'''


for i in range(97,123):
   print(f'%d e %s' % (i,chr(i)))
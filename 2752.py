'''
Su profesor le gustaría que usted hiciera un programa con las siguientes características:
   Cree una variable para almacenar 50 caracteres;
   Asigne la variable anterior a la frase: "AMO FAZER EXERCICIO NO URI";
   Muestra en la primera línea el carácter <, el valor almacenado en la variable con el formato "% s" y el carácter>;
   Muestre en la línea siguiente el carácter <, el valor almacenado en la variable con el formato "% 30s" y el carácter>;
   Muestre en la línea siguiente el carácter <, el valor almacenado en la variable con el formato "% .20s" y el carácter>;
   Muestre en la línea siguiente el carácter <, el valor almacenado en la variable con el formato "% -20s" y el carácter>;
   Muestre en la línea siguiente el carácter <, el valor almacenado en la variable con el formato "% -30s" y el carácter>;
   Muestre en la línea siguiente el carácter <, el valor almacenado en la variable con el formato "% .30s" y el carácter>;
   Muestre en la línea siguiente el carácter <, el valor almacenado en la variable con el formato "% 30.20s" y el carácter>;
   Muestre en la línea siguiente el carácter <, el valor almacenado en la variable con el formato "% -30.20s" y el carácter>;
Entrada
No hay.

Salida
El resultado de su programa debe ser escrito según el ejemplo de la salida.
'''

a = 'AMO FAZER EXERCICIO NO URI'
b = 'AMO FAZER EXERCICIO'
print(f'<{a}>\n<    {a}>\n<{b} >\n<{a}>\n<{a}    >\n<{a}>\n<          {b} >\n<{b}           >')
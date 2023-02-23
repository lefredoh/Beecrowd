'''
Tía Joana es una profesora respetada y tiene varios alumnos. En su última clase, prometió que rifaría a un estudiante para ganar un bono especial en la calificación final: puso N hojas de papel numeradas del 1 al N en una bolsa y dibujó un cierto número K; el estudiante ganador fue el K-ésimo alumno en el pase de lista.

El problema es que a la tía Joana se le olvidó el diario de clases, por lo que no tiene forma de saber qué número corresponde a qué alumno. Sabe los nombres de todos los alumnos, y que sus números, del 1 al N, están asignados alfabéticamente, pero sus alumnos están muy ansiosos y quieren saber quién es el ganador.

Dados los nombres de los estudiantes de Tía Joana y el número sorteado, determine el nombre del estudiante que debe recibir el bono.

Entrada
La primera línea contiene dos números enteros N y K separados por un espacio en blanco (1 ≤ K ≤ N ≤ 100). Cada una de las siguientes N líneas contiene una cadena de texto con longitud mínima 1 y longitud máxima 20 que representa los nombres de los estudiantes. Los nombres se componen de todas las letras minúsculas de la 'a' a la 'z'.

Salida
Su programa debe imprimir una sola línea, que contenga el nombre del estudiante que recibirá el bono.
'''

n = list(map(int,input().rstrip().split()))
lista = []
for i in range(n[0]):
   l = input()
   lista.append(l)

lista.sort()

print(lista[n[1]-1])
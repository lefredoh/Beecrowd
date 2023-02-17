'''Vitória y su indecisión

Por Gustavo Ribeiro, IFPB - Campina Grande BR Brasil
Límite de tiempo: 1

No hay nadie en el mundo más indeciso que Vitória. A pesar de que sabe que es una gran programadora, como una de las que tienen muchos proyectos en el campo de TI publicados y muchos otros en 
proceso de escritura, no está segura de si será una programadora profesional. Hay noches que quiere estudiar Ciencias de la Computación (Ciência da Computação, en portugués), hay días que 
quiere estudiar algo de Ingeniería, algunos días incluso habla de tomar algún curso de Humanidades, ¡qué pecado! Pero usted puede ayudarla a tomar la decisión correcta. Su tarea es simple, 
se le dará una lista con los cursos de licenciatura que Vitória tiene en duda, el resultado debe ser el curso que debe elegir.

Input
La primera línea de la entrada es un número entero 1 ≤ n ≤ 2000, que representa el número de cursos que se deben considerar. Cada una de las siguientes n líneas, hay un curso S, 1 ≤ |S| ≤ 100, 
el nombre de uno de los cursos Vitória está en duda.

Output
Escriba el nombre del curso que Vitória debe tomar en portugués sin acentuación.'''

n = int(input())
for i in range(n):
   c = input()

print('Ciencia da Computacao')
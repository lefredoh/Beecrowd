'''
Toorg is the wisest member of the group of heroes called The Protectors of the Milky Way. For any question, it has the ideal answer! Write a program that, given a question, tells 
Toorg's answer.

Input
The input will have several test cases. For each test case, a N number is displayed, which represents the number of test cases. Then there will be N lines, with questions asked for Toorg.

Output
For each test case, print Toorg's answer.
'''

n = int(input())
lista= []
for i in range(n):
   l = input()
   lista.append('I am Toorg!')


for i in lista:
   print(i)
objeto = {'1001':1.5,'1002':2.5,'1003':3.5,'1004':4.5,'1005':5.5}

suma = 0
n = int(input())
for i in range(n):
   num = list(map(int,input().rstrip().split()))
   suma+=float(objeto[str(num[0])])*float(num[1])

print(f'{suma:.2f}')

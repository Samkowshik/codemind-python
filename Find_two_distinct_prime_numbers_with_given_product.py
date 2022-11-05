import math
def pri(n):
    for i in range(2,n):
        if n%i==0 and n!=1:
            return 0
    else:
        return 1
n=int(input())
for i in range(2,int(math.sqrt(n))+2):
    if i*(n//i)==n and pri(i)==1 and pri(n//i)==1:
        print(i,n//i)
        break
else:
    print(-1)
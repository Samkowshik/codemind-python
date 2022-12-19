def pri(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
for t in range(int(input())):
    n=int(input())
    i=j=n
    while 1:
        if pri(i):
            print(i)
            break
        i-=1
        if pri(j):
            print(j)
            break
        j+=1
        
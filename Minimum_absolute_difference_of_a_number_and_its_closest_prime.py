def pri(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
i=j=n
if pri(n):
    print('0')
else:
    while 1:
        i-=1
        if pri(i):
            print(n-i)
            break
        j+=1
        if pri(j):
            print(j-n)
            break
        
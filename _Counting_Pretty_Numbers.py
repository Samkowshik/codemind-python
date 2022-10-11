t=int(input())
for i in range(t):
    n1,n2=map(int,input().split())
    c=0
    for i in range(n1,n2+1):
        if i%10==2 or i%10==3 or i%10==9:
            c+=1;
    print(c)       
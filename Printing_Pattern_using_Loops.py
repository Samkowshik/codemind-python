n=int(input())
x=n
for i in range(1,n+1):
    x=n
    for j in range(1,n+1):
        print(x,end=' ')
        if i>j:
            x-=1
    for j in range(2,n+1):
        if j>x:
            x+=1
        print(x,end=' ')
    print()
for i in range(2,n+1):
    x=n
    for j in range(1,n+1):
        print(x,end=' ')
        if i+j<n+1:
            x-=1
    for j in range(3,n+2):
        print(x,end=' ')
        if j>x:
            x+=1
    print()
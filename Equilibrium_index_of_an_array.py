for t in range(int(input())):
    n=input()
    l=list(map(int,input().split()))
    s=sum(l)
    x=0
    for i in l:
        if x==(s-i)/2:
            print(l.index(i))
            break
        x+=i
    else:
        print(-1)
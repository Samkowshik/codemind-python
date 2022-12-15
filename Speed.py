for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=l[0]
    c=1
    for i in l:
        if i<m:
            m=i
            c+=1
    print(c)
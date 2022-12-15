for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        if sum(l[:i])==sum(l[i+1:]):
            print('YES')
            break
    else:
        print('NO')
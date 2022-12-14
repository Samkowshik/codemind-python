for t in range(int(input())):
    n=input()
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.extend(l2)
    l1.sort()
    print(*l1)
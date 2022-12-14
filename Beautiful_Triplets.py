n=int(input())
l=(list(map(int,input().split())))
while len(l):
    print(len(l))
    m=min(l)
    while m in l:
        l.remove(m)
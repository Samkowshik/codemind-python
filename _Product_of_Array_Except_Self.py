n=int(input())
l=list(map(int,input().split()))
m=1
for i in l:
    m*=i
for i in l:
    print(m//i,end=' ')
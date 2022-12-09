n=int(input())
lst=list(map(int,input().split()))
z=0
for i in range(n):
    for j in range(n):
        if(i!=j and lst[i]==lst[j]):
            z=1
            print(lst[i])
            break
    if(z==1):
        break